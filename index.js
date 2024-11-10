
const express = require("express");
const { spawn } = require("child_process");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
const port = 5000;

app.use(bodyParser.json());
app.use(cors({ origin: "http://localhost:3000" }));

app.post("/analyze", (req, res) => {
    const userInput = req.body.input;

    // Spawn a new Python process for each request
    const childPython = spawn("python", ["analyze.py", userInput]);
    
    let output = "";

    // Listen for data from stdout
    childPython.stdout.on("data", (data) => {
        output += data.toString();
    });

    // Handle process completion and send response
    childPython.on("close", (code) => {
        if (code !== 0) {
            console.error("Python script failed with code:", code);
            return res.status(500).json({ error: "Python script failed" });
        }
        // Send the accumulated output back to the frontend
        res.json({ result: output });
    });

    // Handle any errors from the Python script
    childPython.stderr.on("data", (data) => {
        console.error("Error from Python script:", data.toString());
    });
});

app.get("/", (req, res) => {
    res.send("Server is running");
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});



 /** load the http mdoule  using plain node js
// Load HTTP module
const http = require("http");

const hostname = "127.0.0.1";
const port = 8000;

// Create HTTP server
const server = http.createServer(function (req, res) {
  // Set the response HTTP header with HTTP status and Content type
  res.writeHead(200, { "Content-Type": "text/plain" });

  // Send the response body "Hello World"
  res.end("Hello World\n");
});

// Prints a log once the server starts listening
server.listen(port, hostname, function () {
  console.log(`Server running at http://${hostname}:${port}/`);
});*/
