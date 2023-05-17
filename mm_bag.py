import networkx as nx
import matplotlib.pyplot as plt

# Get user inputs for main idea and sub-ideas
main_idea = input("Enter the main idea: ")
sub_ideas = input("Enter sub-ideas (comma-separated): ").split(",")

# Create a directed graph
mindmap = nx.DiGraph()

# Add nodes (ideas) to the mindmap
mindmap.add_node(main_idea)
for sub_idea in sub_ideas:
    mindmap.add_node(sub_idea.strip())

# Add edges to connect the ideas
for sub_idea in sub_ideas:
    mindmap.add_edge(main_idea, sub_idea.strip())

# Draw the mindmap
pos = nx.spring_layout(mindmap)
nx.draw(mindmap, pos, with_labels=True, node_color='lightblue',
        node_size=1500, font_size=10, font_weight='bold', edge_color='gray')
plt.show()
