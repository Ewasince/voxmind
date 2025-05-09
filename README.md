# 🗣 voxmind

Project for extend llm assistants with external integrations

# 🛠️ Install

```shell
pip install 'git+https://github.com/Ewasince/voxmind'
```

# 🚀 Quick start

```python
############### prepare assistant ###############

## load settings
from voxmind.app_utils.settings import Settings

settings = Settings()

## create commands source (available from cli or voice commands)
from voxmind.app_interfaces.command_source import CommandSource
from voxmind.commands_sources.cli_command_source import CLICommandSource

command_source: CommandSource = CLICommandSource(settings=settings)

## create llm module
from voxmind.app_interfaces.llm_module import LLMClient
from voxmind.llm_clients.gigachat_client import GigaChatClient

gpt_module: LLMClient = GigaChatClient(Settings())

## topic definer, which determines which command need to activate. Uses llm module
from voxmind.app_interfaces.topic_definer import TopicDefiner
from voxmind.topic_definers.llm_based import TopicDefinerGPT

topic_definer: TopicDefiner = TopicDefinerGPT(gpt_module)

## create command recognizer, which recognize command by using topic definer
from voxmind.assistant_core.command_recognizer import CommandRecognizer

command_recognizer: CommandRecognizer = CommandRecognizer(topic_definer)

############### setup commands ###############
from voxmind.app_interfaces.command_performer import CommandPerformer

## add example commands
from voxmind.base_commands.get_current_os import CommandGetCurrentOS

command_os: CommandPerformer = CommandGetCurrentOS()
command_recognizer.add_command(command_os.command_topic, command_os)

from voxmind.base_commands.get_current_time import CommandGetCurrentTime

command_time: CommandPerformer = CommandGetCurrentTime()
command_recognizer.add_command(command_time.command_topic, command_time)

from voxmind.base_commands.llm_question import CommandLLMQuestion

command_default: CommandPerformer = CommandLLMQuestion(gpt_module)
command_recognizer.add_command(None, command_default)

############### run assistant ###############
command_text: str
async for command_text in command_source:
    command_result = await command_recognizer.process_command_from_text(command_text)

    if command_result is None:
        continue

    print(f"Assistant answer > {command_result}")

```