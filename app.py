from flask import Flask
import matplotlib.pyplot as plt
app=Flask(__name__)

@app.route('/')
def main():
    return 'Hello, world!'

@app.route('/graph')
def graph():
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 5, 3, 5, 7, 8]

    plt.plot(x, y)
    plt.show()

    plt.savefig("output.jpg")
    print("succesfully built, shown, and saved graph as jpg")
    return("succesfully built, shown, and saved graph as jpg")

if __name__ == '__main__':
        print("HELLO WORLD! BUILT WITH A p2i file")
        app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
