from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import CompleteStyle
from .completer import CustomCompleter
from utils.core.color import ColorSelected
from os import getuid


if getuid() == 0:
    session = PromptSession(history=FileHistory("/tmp/homeS_historyroot"))
else:
    session = PromptSession(history=FileHistory("/tmp/homeS_history"))


def prompt(commands, module=None):
    """启动具有给定命令的提示符

    Args:
        commands ([str]): 自动完成的命令列表
        module (str, optional): 模块名称。默认为None。

    Returns:
        prompt session: 提示符会话
    """
    default_prompt = "ragdoll"
    color_default_prompt = ColorSelected().theme.primary
    warn = ColorSelected().theme.warn
    confirm = ColorSelected().theme.confirm
    html = HTML(f"<bold><{color_default_prompt}>{default_prompt} >></{color_default_prompt}></bold>")
    if module:
        html = HTML(
            f"<bold><{color_default_prompt}>{default_prompt}</{color_default_prompt}> (<{warn}>{module}</{warn}>) <{confirm}>>></{confirm}></bold> ")

    data = session.prompt(
        html,
        completer=CustomCompleter(commands),
        complete_style=CompleteStyle.READLINE_LIKE,
        auto_suggest=AutoSuggestFromHistory(),
        enable_history_search=True)
    return data
