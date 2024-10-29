def tower_of_hanoi(n, source, target, auxiliary):
    """Solve the Tower of Hanoi problem."""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary, using target as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    # Move the n-1 disks from auxiliary to target, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage
if __name__ == "__main__":
    num_disks = int(input("Enter the number of disks: "))
    tower_of_hanoi(num_disks, 'A', 'C', 'B')  # A, C and B are names of rods
