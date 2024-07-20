def read_feedback_files(file_names):
    feedback_data = []
    for file_name in file_names:
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    name, rating, comment = line.strip().split(':')
                    feedback = {
                        'name': name,
                        'rating': int(rating),
                        'comment': comment
                    }
                    feedback_data.append(feedback)
        except FileNotFoundError:
            print(f"Error: The file {file_name} could not be found or opened.")
        except Exception as e:
            print(f"An error occurred: {e}")
    return feedback_data

# Example usage:
file_names = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']
feedback_list = read_feedback_files(file_names)

