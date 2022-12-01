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

import streamlit as st


def before():
    st.markdown(
        """
Postgresql is one of the most popular flavors of SQL. Streamlit provides an officially supported postgresql connection adapter.

- It can be installed via `pip install streamlit-connect-postgres`
- Source code and more docs can be found at [github.com/streamlit/connect-postgres](http://github.com/streamlit/connect-postgres)

The connection adapter is built on psycopg2-binary, alternative community supported adapters can be found [here](#).

This wizard will set up the basic connection parameters for a PostgreSQL database.
    """
    )


def after():
    st.markdown(
        """
Please remember to ensure `streamlit-connect-postgres` (or another compatible adapter) is installed for your app before attempting to use the connector!

```sh
pip install streamlit-connect-postgres
```

If everything is set up correctly, you can get started with just a few lines of code:

```python
import streamlit as st
conn = st.connection('postgresql')

df = conn.query('select * from ab_data order by random() limit 500')
st.dataframe(df)
```

Press the button below to get started with an example Postgres app that works with public data.
    """
    )

    st.button("⚡ Set up sample postgres app!")

    "Launch the app with:"
    st.code("streamlit run psql_sample.py")
