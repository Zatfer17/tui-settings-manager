from textual.app import App, ComposeResult
from textual.widgets import Footer, OptionList
from textual.containers import Container, VerticalScroll
from tui_settings_manager.features.settings.settings import Settings


settings = Settings()

class SettingsWidget(VerticalScroll):

    BORDER_TITLE = "Settings"

    def compose(self) -> ComposeResult:
        yield OptionList(*settings.get_options())

class OptionListApp(App):

    BORDER_TITLE = "Settings manager app"
    CSS_PATH = "static/style.tcss"

    def compose(self) -> ComposeResult:
        yield Container(
            SettingsWidget(can_focus=False, can_focus_children=True)
        )
        yield Footer()

    def on_option_list_option_selected(self, message: OptionList.OptionSelected) -> None:
        settings.run_option(message.option.prompt)


def settings_manager_app() -> None:
    app = OptionListApp()
    app.run()