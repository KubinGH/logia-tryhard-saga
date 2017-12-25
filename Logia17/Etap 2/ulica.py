def maksos(A):
    best_count = current_count = 1
    first_counted = False; first_count = 1
    for last, current in zip(A, A[1:]):
        if current - last <= 3:
            current_count += 1
            best_count = max(best_count, current_count)
        else:
            if not first_counted:
                first_count = current_count
                first_counted = True
            current_count = 1
    if first_counted:
        current_count += first_count
        best_count = max(best_count, current_count)
    return best_count

if __name__ == "__main__":
    print(maksos([1,4,7,11,13,14,15,16,20]))
    print(maksos([1,4,7,13,14,15,20]))
