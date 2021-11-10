import pytest
from django.test import Client

from company.models import CompanyName, CompanyTag, Company, Language, Tag


@pytest.fixture
def api():
    return Client()


@pytest.fixture(scope='function')
def autocomplete_context(db):
    language = Language.objects.create(name='ko')
    company1 = Company.objects.create(id=1)
    company2 = Company.objects.create(id=2)
    CompanyName.objects.create(name='주식회사 링크드코리아', company=company1, language=language)
    CompanyName.objects.create(name='스피링크', company=company2, language=language)


@pytest.fixture(scope='function')
def search_context(db):
    language1 = Language.objects.create(name='ko')
    language2 = Language.objects.create(name='en')
    company = Company.objects.create(id=3)
    CompanyName.objects.create(name='원티드랩', company=company, language=language1)
    CompanyName.objects.create(name='Wantedlab', company=company, language=language2)
    tag1 = Tag.objects.create(name='태그_4', language=language1)
    tag2 = Tag.objects.create(name='태그_20', language=language1)
    tag3 = Tag.objects.create(name='태그_16', language=language1)
    CompanyTag.objects.create(tag=tag1, company=company)
    CompanyTag.objects.create(tag=tag2, company=company)
    CompanyTag.objects.create(tag=tag3, company=company)


# @pytest.mark.django_db()
def test_company_name_autocomplete(api, autocomplete_context):
    """
    1. 회사명 자동완성
    회사명의 일부만 들어가도 검색이 되어야 합니다.
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = api.get("/search", content_type='application/json', data={'query': '링크'}, **{"HTTP_x-wanted-language": "ko"})
    searched_companies = resp.data

    assert resp.status_code == 200
    assert searched_companies == [
        {"company_name": "주식회사 링크드코리아"},
        {"company_name": "스피링크"},
    ]


# @pytest.mark.django_db()
def test_company_search(api, search_context):
    """
    2. 회사 이름으로 회사 검색
    header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = api.get("/companies/Wantedlab", content_type='application/json', **{"HTTP_x-wanted-language": "ko"})
    company = resp.data
    assert resp.status_code == 200
    assert company == {
        "company_name": "원티드랩",
        "tags": [
            "태그_4",
            "태그_20",
            "태그_16",
        ],
    }

    # 검색된 회사가 없는경우 404를 리턴합니다.
    resp = api.get("/companies/없는회사", content_type='application/json', **{"HTTP_x-wanted-language": "ko"})
    assert resp.status_code == 404


@pytest.mark.django_db()
def test_new_company(api):
    """
    3.  새로운 회사 추가
    새로운 언어(tw)도 같이 추가 될 수 있습니다.
    저장 완료후 header의 x-wanted-language 언어값에 따라 해당 언어로 출력되어야 합니다.
    """
    resp = api.post(
        "/companies",
        data={
            "company_name": {
                "ko": "라인 프레쉬",
                "tw": "LINE FRESH",
                "en": "LINE FRESH",
            },
            "tags": [
                {
                    "tag_name": {
                        "ko": "태그_1",
                        "tw": "tag_1",
                        "en": "tag_1",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_8",
                        "tw": "tag_8",
                        "en": "tag_8",
                    }
                },
                {
                    "tag_name": {
                        "ko": "태그_15",
                        "tw": "tag_15",
                        "en": "tag_15",
                    }
                }
            ]
        },
        content_type='application/json',
        **{"HTTP_x-wanted-language": "tw"}
    )

    company = resp.data
    assert company == {
        "company_name": "LINE FRESH",
        "tags": [
            "tag_1",
            "tag_8",
            "tag_15",
        ],
    }
