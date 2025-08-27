from rsa_transfer import test_rsa
from ecc_transfer import test_ecc

def run_tests():
    print("🔒 SECURE FILE TRANSFER TESTING\n")
    test_files = ["test_files/file_1MB.txt", "test_files/file_10MB.txt"]

    for file in test_files:
        test_rsa(file)
        test_ecc(file)

if __name__ == "__main__":
    run_tests()
