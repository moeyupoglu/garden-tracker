<!DOCTYPE html>
<html>
<body>
	<h1>Garden Tracker</h1>
	<h2>Description</h2>
	<p>Garden Tracker is a tool for helping users track and manage the plants in their garden. With Garden Tracker, users can easily keep track of the plants in their garden</p>
	<h2>Features</h2>
	<ul>
		<li>Search for Plants by Name</li>
		<li>Create an account to save favorite plants</li>
		<li>Add new plant to the database</li>
		<li>Edit and delete existing plants</li>
		<li>View information for each plant</li>
	</ul>
	<h2>Technologies Used</h2>
	<ul>
		<li>Python</li>
		<li>FastAPI framework</li>
		<li>PostgreSQL database</li>
		<li>SQLAlchemy ORM</li>
		<li>Jinja2 templating engine</li>
		<li>HTML, CSS, and JavaScript</li>
	</ul>
	<h2>Getting Started</h2>
	<h3>Prerequisites</h3>
	<ul>
		<li>Python 3.8 or higher</li>
		<li>PostgreSQL database</li>
	</ul>
	<h3>Installation</h3>
	<ol>
		<li>Clone this repository: <code>git clone https://github.com/moeyupoglu/garden-tracker.git</code></li>
		<li>Navigate to the project directory: <code>cd garden-tracker</code></li>
		<li>Create a virtual environment: <code>python -m venv venv</code></li>
		<li>Activate the virtual environment: <code>source venv/bin/activate</code></li>
		<li>Install dependencies: <code>pip install -r requirements.txt</code></li>
	</ol>
	<h3>Usage</h3>
	<ol>
		<li>Start the application: <code>python main.py</code></li>
		<li>Open a web browser and navigate to <a href="http://localhost:8000">http://localhost:8000</a></li>
	</ol>
	<h3>Configuration</h3>
	<p>To configure the application, create a <code>.env</code> file in the project directory and set the following environment variables:</p>
	<ul>
		<li><code>DATABASE_HOSTNAME</code>: the name of your PostgreSQL database</li>
		<li><code>DATABASE_PORT</code>: Port number used for database</li>
		<li><code>DATABASE_PW</code>: Password used for database</li>
		<li><code>DATABASE_USERNAME</code>: User database </li>
        <li><code>SECRET_KEY</code>: A Secret Key </li>
        <li><code>ALGORITHM</code>: Algorithm for JWT TOKEN </li>
        <li><code>ACCESS_TOKEN_EXPIRE_MINUTES</code>: Expiry Time for access token </li>
	</ul>
	<h2>Contributing</h2>
	<p>Contributions to Garden Tracker are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.</p>
	<h2>License</h2>
	<p>Garden Tracker is licensed under the MIT License. See <code>LICENSE</code> for details.</p>
	<h2>Authors</h2>
	<p>Muhammad Eyupoglu(<a href="mailto:muhammad.magh@gmail.com">muhammad.magh@gmail.com</a>)</p>
	<h2>Acknowledgements</h2>
	<p>Special thanks to the instructors and teaching assistants of the Python programming course.</p>
</body>
</html>
