# Building a Digital Family Tree: An Application of Graph Data Structures  
**By: Lelin Zheng, Jiachen Xu, and Zeynab Idris**  

This project enables users to create, manage, and visualize their own family tree. It incorporates graph data structures to efficiently model relationships, allowing for searches (like finding the relationship path between two family members using BFS) and visualizations.  

---

## Features  

- **Create and Manage a Family Tree**  
  - Add, update, or remove family members.  
  - Add or delete immediate relationships between members.  

- **Search for Relationships**  
  - Retrieve the relationship path between two family members using the **Breadth-First Search (BFS)** algorithm.  

- **Visualization**  
  - Visualize the family tree as a graph.  

- **Demo Families**  
  - Pre-built **Kardashian Family Tree** with 30 members.  
  - A small family demo for Zeynab with fewer members.  

- **Data Persistence**  
  - Save family data to a JSON file for future use.  
  - Load existing family data from a JSON file.  

---

## File Structure  

```plaintext
digital-family-tree/
│
├── family.py                     # Core logic for managing the family tree
├── person.py                     # Defines the Person class and attributes
├── graph.py                      # Family tree visualization functions
├── menu.py                       # Command-line menu for user interaction
├── main.py                       # Entry point of the program
│
├── build_kardashian_family.py    # Script to build Kardashian family data
├── build_zeynab_family.py        # Script to build Zeynab's small family data
├── demo_zeynab_family_graph.py   # Visualizes Zeynab's family graph
│
├── family_test.py                # Unit tests for the Family class
├── person_test.py                # Unit tests for the Person class
│
└── data/
    ├── kardashian_family_tree.json  # Demo: Kardashian family with 30 members
    └── zeynab_small_family.json     # Demo: Zeynab's small family data
```

---

## Demo  

### Menu Interface  
The program starts with a command-line interface that allows users to select actions like creating a family, searching for relationships, or visualizing the family graph.  

**Main Menu Example:**  
```plaintext
Please choose one of the following options:

1. Add a new person to your family tree  
2. Remove a person from your family tree  
3. Add immediate relationship for a person  
4. Remove immediate relationship for a person  
5. Update a person's information  
6. Find the relationship (path) between two people  
7. Look up a person's information  
8. Visualize your family tree  
9. Save the data into a new or existing JSON file  
10. Exit the program  
```

---

## Demo Visualization  

Here’s an example graph visualization for the Kardashian Family:  

![Kardashian Family Graph](https://github.com/LelinZheng/Family-Graph-Project/blob/webApp/demo_kardashian_family_graph.png)

---

## Future Improvements  

- **Enhanced Features**  
  - Identify the **most popular occupation** in the family.  
  - Alert for **birthdays** in the upcoming month.  
  - Search for people with the **same occupation** or **birth month**.  

- **Interactive Visualization**  
  - Enhance graph visualization with interactive tools (e.g., NetworkX or PyVis).  

- **Frontend Development**  
  - Develop a web-based frontend for a better user experience using **Django** or other web frameworks.  

---

## Usage  

1. **Run the Program**  
   Start the program using:  
   ```bash
   python main.py
   ```

2. **Load Demo Families**  
   - Load the Kardashian Family Tree or Zeynab's family from the `data` folder when prompted.  

3. **Visualize**  
   Use the menu options to visualize the family tree graph.  

---

## Dependencies  

This project primarily uses Python libraries:  

- `datetime`  
- `json`  
- `os`  
- `NetworkX`
---

## Contributors  

- Jiachen Xu  
- Lelin Zheng  
- Zeynab Idris  
