# AsyncChromiumLoader 사용
import streamlit as st
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer

st.set_page_config(page_title="SiteGPT", page_icon="👀")

html2text_transformer = Html2TextTransformer()

st.markdown(
    """
    # SiteGPT

    웹사이트의 컨텐츠를 검색하세요.
    왼쪽 사이드바에 URL 을 입력해서 시작하세요.
    """
)

with st.sidebar:
    url = st.text_input(label="Write down a URL", placeholder="https://exmaple.com")

if url:
    loader = AsyncChromiumLoader([url])
    docs = loader.load()
    transformed = html2text_transformer.transform_documents(docs)
    st.write(transformed)


# SitemapLoader 사용 - 사용하기 엄청 까다로워서 안하는게 좋을 듯, ssl 인증 문제, 특정 사이트는 아예 접근이 안되는 경우도 있음
# import streamlit as st
# from langchain_community.document_loaders import SitemapLoader

# st.set_page_config(page_title="SiteGPT", page_icon="👀")


# def load_website(url):
#     loader = SitemapLoader(url, verify_ssl=False)
#     loader.requests_per_second = 2
#     docs = loader.load()
#     return docs


# st.markdown(
#     """
#     # SiteGPT

#     웹사이트의 컨텐츠를 검색하세요.
#     왼쪽 사이드바에 URL 을 입력해서 시작하세요.
#     """
# )

# with st.sidebar:
#     url = st.text_input(label="Write down a URL", placeholder="https://exmaple.com")

# # https://api.python.langchain.com/sitemap.xml
# if url:
#     if ".xml" not in url:
#         st.error("Sitemap URL 을 입력해주세요.")
#     else:
#         docs = load_website(url)
#         st.write(docs)
