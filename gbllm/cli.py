""" Command line interface for the gbllm package. """
import click


@click.group(invoke_without_command=True)
@click.option('--instruction', help='Instruction to execute LLM.', prompt='Instruction to execute LLM.')
@click.option('--genbank', help='Genbank file to use.', prompt='Genbank file to use.')
def main(instruction: str, genbank: str) -> None:
    """ Entry point for the command line interface. """

    from gbllm.main import run_gbllm

    run_gbllm(instruction=instruction, genbank=genbank)


if __name__ == '__main__':
    main()
