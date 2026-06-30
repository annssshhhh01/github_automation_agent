from src.registry.capability_registry import CapabilityRegistry

registry = CapabilityRegistry()

registry.register_native(
    name="create_issue",
    description="Create a GitHub Issue",
    entrypoint="src.tools.native.create_issue",
)

registry.register_native(
    name="list_issues",
    description="List repository issues",
    entrypoint="src.tools.native.list_issues",
)

registry.register_native(
    name="get_repository",
    description="Retrieve repository information",
    entrypoint="src.tools.native.get_repo",
)

print()

for capability in registry.list_capabilities():

    print(capability.name)

    print(capability.capability_type)

    print(capability.entrypoint)

    print("-" * 40)
