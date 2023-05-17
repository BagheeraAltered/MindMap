import networkx as nx
import matplotlib.pyplot as plt

# Recursive function to add sub-ideas and sub-sub-ideas to the mindmap


def add_sub_ideas(mindmap, parent_idea):
    sub_ideas = input(
        f"Enter sub-ideas for {parent_idea} (comma-separated, or enter to skip): ").split(",")

    for sub_idea in sub_ideas:
        sub_idea = sub_idea.strip()

        if sub_idea:
            mindmap.add_node(sub_idea)
            mindmap.add_edge(parent_idea, sub_idea)
            add_sub_ideas(mindmap, sub_idea)


# Get user input for the main idea
main_idea = input("Enter the main idea: ")

# Create a directed graph
mindmap = nx.DiGraph()

# Add the main idea to the mindmap
mindmap.add_node(main_idea)

# Call the recursive function to add sub-ideas and sub-sub-ideas
add_sub_ideas(mindmap, main_idea)

# Draw the mindmap
pos = nx.spring_layout(mindmap)
nx.draw(mindmap, pos, with_labels=True, node_color='lightblue',
        node_size=1500, font_size=10, font_weight='bold', edge_color='gray')
plt.show()
