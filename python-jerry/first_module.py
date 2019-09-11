print("This will always be run.")

def main():
    print("First Module's Main Method")
    print("First Module's Name: {}".format(__name__))
   

if __name__ == "__main__":
    print("Run Directly")
    main()
else:
    print("Run From Import")
