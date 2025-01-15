async function fetchRegistry() {
    const response = await fetch("/api/get_registry");
    const registry = await response.json();
    populateRegistryTree(registry);
}

function populateRegistryTree(registry, parentElement = document.getElementById("registry-tree")) {
    parentElement.innerHTML = "";
    for (const key in registry) {
        const li = document.createElement("li");
        li.textContent = key;
        parentElement.appendChild(li);

        if (Object.keys(registry[key]).length > 0) {
            const ul = document.createElement("ul");
            li.appendChild(ul);
            populateRegistryTree(registry[key], ul);
        }
    }
}

// Fetch and display the registry on page load
window.onload = fetchRegistry;
