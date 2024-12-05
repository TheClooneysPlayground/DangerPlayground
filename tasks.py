from invoke import task

"""
As a record of what commands I have been running
"""


@task
def create_library(c, name):
    command = f"""
    swift package init \
    --type library \
    --enable-swift-testing \
    --name {name}
    """

    print(command)

    c.run(command)
