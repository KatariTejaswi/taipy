# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from .config import Config


# Default config loaded by app.py
default_config: Config = {
    "allow_unsafe_werkzeug": False,
    "async_mode": "gevent",
    "change_delay": None,
    "chart_dark_template": None,
    "dark_mode": True,
    "dark_theme": None,
    "debug": False,
    "extended_status": False,
    "favicon": None,
    "flask_log": False,
    "host": "127.0.0.1",
    "light_theme": None,
    "margin": "1em",
    "ngrok_token": "",
    "notification_duration": 3000,
    "propagate": True,
    "run_browser": True,
    "run_in_thread": False,
    "run_server": True,
    "single_client": False,
    "system_notification": False,
    "theme": None,
    "time_zone": None,
    "title": None,
    "stylekit": False,
    "stylekit_variables" : {
        # Primary and secondary colors
        "color_primary": "#ff462b",
        "color_secondary": "#283282",

        # Contextual color
        "color_error": "#FF595E",
        "color_warning": "#FAA916",
        "color_success": "#96E6B3",

        # Background and elevation color for LIGHT MODE
        "color_background_light": "#f1f1f1",
        "color_paper_light": "#ffffff",

        # Background and elevation color for DARK MODE
        "color_background_dark": "#051924",
        "color_paper_dark": "#072636",

        # DEFINING FONTS

        # Set main font family
        "font_family": "Lato, Arial, sans-serif",

        # DEFINING SHAPES

        # Base border radius
        "border_radius": 8,

        # DEFINING MUI COMPONENTS STYLES

        # Matching input and button height
        "input_button_height": 48
    },
    "upload_folder": None,
    "use_arrow": False,
    "use_reloader": False,
    "watermark": "Taipy inside",
    "webapp_path": None,
    "port": 5000,
}
