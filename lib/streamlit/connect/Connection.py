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

import toml

import streamlit as st
import streamlit.connect.supported as supported
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Streamlit Connection Wizard",
        page_icon="🔌",
    )

    st.subheader("Let's connect 🔌 to some data!")

    curr_connections = toml.load("./.streamlit/secrets.toml").get("connections", {})

    def clear_state():
        for key in ["create_type", "success", "edit_mode", "existing"]:
            if key in st.session_state:
                del st.session_state[key]

    if "success" in st.session_state:
        st.success(
            f"""Updated connection for {st.session_state['supported'][st.session_state['create_type']]['friendly_name']} in your secrets file"""
        )
        clear_state()

    if "connections" in st.secrets:
        current_conn = st.selectbox("Existing connections", curr_connections.keys())

        edit_mode = st.button("Edit")

    with st.expander("Add a new connection"):
        create_type = ""

        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]

        conn_types = list(supported.connections.keys())
        for i in range(len(conn_types)):
            if cols[i % 3].button(
                supported.connections[conn_types[i]]["friendly_name"]
            ):
                create_type = conn_types[i]

    if create_type:
        clear_state()
        if create_type in curr_connections.keys():
            st.session_state["existing"] = curr_connections[create_type]
            st.session_state["edit_mode"] = True
        st.session_state["create_type"] = create_type

    if edit_mode:
        clear_state()
        st.session_state["existing"] = curr_connections[current_conn]
        st.session_state["create_type"] = current_conn
        st.session_state["edit_mode"] = True

    if "supported" not in st.session_state:
        st.session_state.supported = supported.connections

    if "edit_mode" in st.session_state:
        st.warning("Updating existing connection", icon="⚠️")

    if (
        "success" not in st.session_state
        and "create_type" in st.session_state
        and st.session_state.supported[st.session_state["create_type"]]["required"]
    ):
        ct = st.session_state["create_type"]
        conn_form = st.form("new_connection")
        conn_form.subheader(
            f"Create connection for {st.session_state['supported'][ct]['friendly_name']}"
        )
        output = {}
        with st.expander("Add parameter"):
            with st.form("add_param", clear_on_submit=True):
                new_param = st.text_input("Parameter Name")
                is_secret = st.checkbox("Secret value")
                if st.form_submit_button("Add") and new_param:
                    st.session_state.supported[ct]["required"].append(new_param)
                    if is_secret:
                        st.session_state.supported[ct]["secrets"].append(new_param)

        for field in st.session_state.supported[ct]["required"]:
            type = "default"
            if field in st.session_state.supported[ct]["secrets"]:
                type = "password"
            existing_val = ""
            if "existing" in st.session_state and field in st.session_state.existing:
                existing_val = st.session_state.existing[field]
            output[field] = conn_form.text_input(field, type=type, value=existing_val)
        if conn_form.form_submit_button("Update Connection"):
            current_secrets = toml.load("./.streamlit/secrets.toml")
            if "connections" not in current_secrets:
                current_secrets["connections"] = {}
            current_secrets["connections"][ct] = output
            with open("./.streamlit/secrets.toml", "w") as f:
                toml.dump(current_secrets, f)
            st.session_state["success"] = True
            st.experimental_rerun()


if __name__ == "__main__":
    run()
