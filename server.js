const express = require("express");
const { exec } = require("child_process");
const cors = require("cors");
const path = require("path");

const app = express();
const PORT = 3000;

app.use(cors());

app.get("/", (req, res) => {
  const cwd = path.join(__dirname, "backend");

  const pythonCommand =
    process.platform === "win32" ? "python" : "python3";

  exec(
    `${pythonCommand} app.py`,
    { cwd },
    (error, stdout, stderr) => {
      if (error) {
        console.error(stderr);
        return res
          .status(500)
          .send("Error running Python script");
      }

      res.type("text/plain").send(stdout.trim());
    }
  );
});

app.listen(PORT, () => {
  console.log(
    `Node server running at http://localhost:${PORT}`
  );
});