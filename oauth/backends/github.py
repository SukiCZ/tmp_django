from social_core.backends.github import GithubOAuth2
from social_core.utils import handle_http_errors


class GitHubOAuth2(GithubOAuth2):
    @handle_http_errors
    def do_auth(self, access_token, *args, **kwargs):
        access_token = self.exchange_code_for_access_token(access_token)
        return super(GitHubOAuth2, self).do_auth(access_token, *args, **kwargs)

    @handle_http_errors
    def exchange_code_for_access_token(self, access_token):
        response = self.request_access_token(
            self.ACCESS_TOKEN_URL,
            data={
                "client_id": self.setting("SOCIAL_AUTH_GITHUB_KEY"),
                "client_secret": self.setting("SOCIAL_AUTH_GITHUB_SECRET"),
                "code": access_token,
                "scope": "user,user:email",
            },
            headers=self.auth_headers(),
            method=self.ACCESS_TOKEN_METHOD,
        )
        self.process_error(response)
        return response["access_token"]
