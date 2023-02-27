from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


def test_counter():
    mock_jobs_file_content = """title,salary,type
Front end developer,2000,trainee
Back end developer,3000,full time
Full stack end developer,4000,full time"""

    with patch("builtins.open", mock_open(read_data=mock_jobs_file_content)):
        assert count_ocurrences("dummy", "Developer") == 3
        assert count_ocurrences("dummy", "developer") == 3
