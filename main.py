from matplotlib import pyplot as plt


def generate_svg_chart(data: dict, output_filename: str = 'graph.svg', width=40, height=10):
    # Separate the data into individual X and Y lists
    x = [item[0] for item in data]
    y = [item[1] for item in data]

    # Create a new figure with customizable dimensions
    fig, ax = plt.subplots(figsize=(width, height))

    # Draw the chart line
    ax.plot(x, y, color='black')

    # Customize the axes and chart title
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Engagement Rate')
    ax.set_title('Engagement Rate Chart')

    # Remove the chart frame
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Save the chart to SVG
    plt.savefig(output_filename, format='svg', bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    # Example usage
    data = [
        ("2023-05-28", 0.5),
        ("2023-05-29", 0.3),
        ("2023-05-30", 0.8),
        ("2023-05-31", 0.6),
        ("2023-06-01", 0.9),
        ("2023-06-28", 0.5),
        ("2023-06-29", 0.3),
        ("2023-06-30", 0.8),
        ("2023-06-31", 0.6),
        ("2023-07-01", 0.9),
        ("2023-07-28", 0.5),
        ("2023-07-29", 0.3),
        ("2023-07-30", 0.8),
        ("2023-07-31", 0.6),
        ("2023-08-01", 0.9),
        ("2023-08-28", 0.5),
        ("2023-08-29", 0.3),
        ("2023-08-30", 0.8),
        ("2023-08-31", 0.6),
        ("2023-09-01", 0.9),
        ("2023-09-28", 0.5),
        ("2023-09-29", 0.3),
        ("2023-09-30", 0.8),
        ("2023-09-31", 0.6),
        ("2023-10-01", 0.9),
        ("2023-10-28", 0.5),
        ("2023-10-29", 0.3),
        ("2023-10-30", 0.8),
        ("2023-10-31", 0.6),
    ]

    generate_svg_chart(data)
