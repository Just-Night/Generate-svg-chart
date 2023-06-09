from matplotlib import pyplot as plt


class ChartGenerator:
    def __init__(
        self,
        output_filename: str = 'graph.svg',
        width: int = 40,
        height: int = 10
    ) -> None:
        self.output_filename = output_filename
        self.width = width
        self.height = height

    def run(self, data: list):
        # Separate the data into individual X and Y lists
        x = [item[0] for item in data]
        y = [item[1] for item in data]

        # Create a new figure with customizable dimensions
        fig, ax = plt.subplots(figsize=(self.width, self.height))

        # Draw the chart line
        ax.plot(x, y, color='black')

        # Removing the axis and label from the graph
        ax.axis('off')

        # Remove the chart frame
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Save the chart to SVG
        plt.savefig(self.output_filename, format='svg', bbox_inches='tight')
        plt.close()


if __name__ == '__main__':
    # Example usage
    data = [
        ('2023-05-01', 0.9),
        ('2023-05-28', 0.5),
        ('2023-05-29', 0.3),
        ('2023-05-30', 0.8),
        ('2023-05-31', 0.6),
    ]

    ChartGenerator().run(data)
