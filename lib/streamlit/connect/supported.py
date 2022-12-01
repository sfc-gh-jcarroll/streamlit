# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit.connect.postgresql as postgresql
import streamlit.connect.s3 as s3

connections = {
    "snowflake": {
        "friendly_name": "Snowflake",
        "required": ["user", "password", "warehouse", "account", "authenticator"],
        "secrets": ["password"],
    },
    "bigquery": {"friendly_name": "Google BigQuery", "required": [], "secrets": []},
    "huggingface": {"friendly_name": "🤗 DataSet", "required": ["user"], "secrets": []},
    "aws_s3": {
        "friendly_name": "AWS S3",
        "required": ["aws_access_key", "aws_secret_key", "region"],
        "secrets": ["aws_secret_key"],
    },
    "http_file": {"friendly_name": "HTTP Download", "required": [], "secrets": []},
    "postgresql": {
        "friendly_name": "PostgreSQL",
        "required": ["user", "dbname", "password", "host"],
        "secrets": ["password"],
    },
    "gsheets": {"friendly_name": "Google Sheets", "required": [], "secrets": []},
    "custom": {"friendly_name": "Custom connection", "required": [], "secrets": []},
}

funcs = {
    "aws_s3": {"before": s3.before, "after": s3.after},
    "postgresql": {"before": postgresql.before, "after": postgresql.after},
}
