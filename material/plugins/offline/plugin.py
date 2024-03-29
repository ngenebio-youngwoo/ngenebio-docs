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

import os

from mkdocs import utils
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin

# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------

# Offline plugin
class OfflinePlugin(BasePlugin):

    # Configuration scheme
    config_scheme = (
        ("enabled", Type(bool, default = True)),
    )

    # Initialize plugin
    def on_config(self, config):
        if not self.config["enabled"]:
            return

        # Ensure correct resolution of links
        config["use_directory_urls"] = False

    # Support offline search
    def on_post_build(self, config):
        if not self.config["enabled"]:
            return

        # Check for existence of search index
        base = os.path.join(config["site_dir"], "search")
        path = os.path.join(base, "search_index.json")
        if not os.path.exists(path):
            return

        # Retrieve search index
        with open(path, "r") as data:
            index = data.read()

            # Inline search index into script
            utils.write_file(
                f"var __index = {index}".encode("utf-8"),
                os.path.join(base, "search_index.js")
            )
