# Copyright (c) 2016-2022 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import logging
import os
import sys

from collections import defaultdict
from markdown.extensions.toc import slugify
from mkdocs import utils
from mkdocs.commands.build import DuplicateFilter
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Tags plugin
class TagsPlugin(BasePlugin):

    # Configuration scheme
    config_scheme = (
        ("tags_file", Type(str, required = False)),
        ("tags_extra_files", Type(dict, default = {})),
    )

    # Initialize plugin
    def on_config(self, config):
        self.tags = defaultdict(list)
        self.tags_file = None
        self.tags_extra_files = []

        # Retrieve tags mapping from configuration
        self.tags_map = config["extra"].get("tags")

        # Use override of slugify function
        toc = { "slugify": slugify, "separator": "-" }
        if "toc" in config["mdx_configs"]:
            toc = { **toc, **config["mdx_configs"]["toc"] }

        # Partially apply slugify function
        self.slugify = lambda value: (
            toc["slugify"](str(value), toc["separator"])
        )

    # Hack: 2nd pass for tags index page(s)
    def on_nav(self, nav, config, files):
        file = self.config.get("tags_file")
        if file:
            self.tags_file = self._get_tags_file(files, file)

        # Handle extra tags index pages, if given
        extra = self.config["tags_extra_files"]
        for file, _ in extra.items():
            self.tags_extra_files.append(
                self._get_tags_file(files, file)
            )

    # Build and render tags index page
    def on_page_markdown(self, markdown, page, config, files):
        if page.file == self.tags_file:
            return self._render_tag_index(markdown, page)

        # Render extra tag files
        if page.file in self.tags_extra_files:
            extra = self.config["tags_extra_files"]
            return self._render_tag_index(
                markdown, page,
                extra.get(page.file.src_path)
            )

        # Add page to tags index
        for tag in page.meta.get("tags", []):
            self.tags[tag].append(page)

    # Inject tags into page (after search and before minification)
    def on_page_context(self, context, page, config, nav):
        if "tags" in page.meta:
            context["tags"] = [
                self._render_tag(tag)
                    for tag in page.meta["tags"]
            ]

    # -------------------------------------------------------------------------

    # Obtain tags file (or extra files)
    def _get_tags_file(self, files, path):
        file = files.get_file_from_path(path)
        if not file:
            log.error(f"Tags file '{path}' does not exist.")
            sys.exit()

        # Add tags file to files
        files.append(file)
        return file

    # Render tags index
    def _render_tag_index(self, markdown, tags_index, allowed = None):
        if not "[TAGS]" in markdown:
            markdown += "\n[TAGS]"

        # Filter tags against allow list, if given
        tags = []
        if allowed:
            for key, value in self.tags.items():
                if self.tags_map.get(key) in allowed:
                    tags.append((key, value))

        # Replace placeholder in Markdown with rendered tags index
        return markdown.replace("[TAGS]", "\n".join([
            self._render_tag_links(tags_index, *args)
                for args in sorted(tags or self.tags.items())
        ]))

    # Render the given tag and links to all pages with occurrences
    def _render_tag_links(self, tags_index, tag, pages):
        classes = ["md-tag"]
        if isinstance(self.tags_map, dict):
            classes.append("md-tag-icon")
            type = self.tags_map.get(tag)
            if type:
                classes.append(f"md-tag-icon--{type}")

        # Render section for tag and a link to each page
        classes = " ".join(classes)
        content = [f"## <span class=\"{classes}\">{tag}</span>", ""]
        for page in pages:

            # Ensure forward slashes, as we have to use the path of the source
            # file which contains the operating system's path separator.
            url = utils.get_relative_url(
                page.file.src_path.replace(os.path.sep, "/"),
                tags_index.file.src_path.replace(os.path.sep, "/")
            )

            # Render link to page
            title = page.meta.get("title", page.title)
            content.append(f"- [{title}]({url})")

        # Return rendered tag links
        return "\n".join(content)

    # Render the given tag, linking to the tags index (if enabled)
    def _render_tag(self, tag):
        type = self.tags_map.get(tag) if self.tags_map else None
        if not self.tags_file or not self.slugify:
            return dict(name = tag, type = type)
        else:
            url = f"{self.tags_file.url}#{self.slugify(tag)}"
            return dict(name = tag, type = type, url = url)

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs")
log.addFilter(DuplicateFilter())
