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
AWS S3 is one of the most popular cloud file stores in use today, and frequently used for storing unstructured or semi-structured
datasets as well as model files.

**You can view our full guide to AWS S3 connections [here](https://docs.streamlit.io/knowledge-base/tutorials/databases/aws-s3).**

## Prerequisites

The S3 connector uses the [AWS Boto3 library](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) installable with pip

```sh
pip install boto3
```
**Credentials**

You will also need to provision AWS credentials, either through the AWS browser console or with support from your system administrator.
Typically a minimum set of credentials include the `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and `AWS_DEFAULT_REGION`. Any region value, such as `us-east-1`,
will usually work for S3 although not for all other AWS services!
    """
    )


def after():
    st.markdown(
        """
Please remember to ensure boto3 is installed for your app before attempting to use the connector!

```sh
pip install boto3
```

If everything is set up correctly, you can get started with just a few lines of code:

```python
import streamlit as st
conn = st.connection('aws_s3', bucket='s3://my_bucket')

st.dataframe(conn.get_object('awesome_data.csv'))
```

Press the button below to get started with an example S3 app that works with public data.
    """
    )

    st.button("⚡ Set up sample S3 app!")

    "Launch the app with:"
    st.code("streamlit run s3_sample.py")
