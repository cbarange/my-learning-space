###### AUTHOR : Clément BARANGER	DATE : 02/01/2020	SOURCE : https://www.linkedin.com/learning/learning-react-js-4/ | Eve PORCELLO

# Learning React

## What is React

React is a javascript library, it open source project build at facebook. Today React is more a framework than a library. React use functional paradigm. To start witj react install _react developer tools_ add-on on your favorite browser. 


## Create your first React page

Here the minimal react setup
```xml
<!DOCTYPE html>
<html>
	<head>
		<title>React Project<title>
		<script type="text/javascript" src="https://unpkg.com/react@16.7.0/umd/react.development.js"></script>
		<script type="text/javascript" src="https://unpkg.com/react-dom@16.7.0/umd/react-dom.development.js"></script>
	</head>
	<body>
		<div id="root"></div>
	</body>
</html>
```

Use react with CDN
```xml
<!DOCTYPE html>
<html>
	<head>
		<title>React Project</title>
		<!-- React library -->
		<script type="text/javascript" src="https://unpkg.com/react@16.7.0/umd/react.development.js"></script>
		<script type="text/javascript" src="https://unpkg.com/react-dom@16.7.0/umd/react-dom.development.js"></script>
		<!-- JSX library -->
		<script type="text/javascript" src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
	</head>
	<body>
		<div id="root"></div>
		<!-- Use React as CDN -->

		<!-- Use Javascript -->
		<!--<script type="text/javascript">
			ReactDOM.render(
				// --- First use ---
				//React.createElement("p",null,"react project tutorial"),
				//document.getElementById("root")
				
				// --- Use properties ---
				//React.createElement("h2",{"style":{"color":"red"}},"hello world"),
				//document.getElementById("root")

				// --- Multi element ---
				//React.createElement("div",null,React.createElement("h1",null,"Hello")),
				//document.getElementById("root")
			)
		</script>-->

		<!-- First use of JSX with Babel -->
		<!--<script type="text/babel">
			ReactDOM.render(
				<h1>Hello Babel</h1>,
				document.getElementById("root")
			)
		</script>-->
		
		<!-- Advence use of JSX with Babel -->
		<!--<script type="text/babel">
			let city = 'Madrid'

			ReactDOM.render(
				/* in JSX use className not class */
				<h1 className="welcomeHeading">Welcome to {city}</h1>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Use component -->
		<!--<script type="text/babel">
			const Hello = () => <div className="welcomeHeading"> <h1>Welcome to React </h1> </div>
			/* You can use differents syntaxs */
			const Hello2 = () => (<div> <h1>Welcome to React 2</h1> </div>)
			/* Or */
			const Hello3 = () =>{return (<div> <h1>Welcome to React 3</h1> </div>)}

			ReactDOM.render(
				/* You can have only one root, component name must use CamelCase */
				<div> <Hello/> <Hello2/> <Hello3/> </div>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Use props -->
		<!--<script type="text/babel">
			const PropsComponent = (props) =>{
				console.log(props) 
				return (<div> <h1>Welcome to {props.country}</h1> <p>{props.name}</p> </div>)
			}
			/* Or */ 
			const PropsComponent2 = ({country, name}) =>{
				return (<div> <h1>Welcome to {country}</h1> <p>{name}</p> </div>)
			}

			ReactDOM.render(
				<PropsComponent2 country="France" name="jean"/>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Multi component -->
		<!--<script type="text/babel">
			const Lake = ({name}) => <h1>{name}</h1>

			const App = () => (
				<div>
					<Lake name="Lake Taheo" />
					<Lake name="Verity lake" />
					<Lake name="Valor lake" />
					<Lake name="Acuity lake" />
				</div>
			)
			
			ReactDOM.render(
				<App/>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Component with class -->
		<!--<script type="text/babel">
			const Lake = ({name}) => <h1>{name}</h1>

			class App extends React.Component {
				state = { loggedIn: true }
				render(){
					return (
						<div>
							<div> The user is {this.state.loggedIn ? "logged in" : "not logged in"}. </div>
							<Lake name="Lake Taheo" />
							<Lake name="Verity lake" />
							<Lake name="Valor lake" />
							<Lake name="Acuity lake" />
						</div>
					)
				}
			}

			ReactDOM.render(
				<App/>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Advence class component -->
		<!--<script type="text/babel">
			const Lake = ({name}) => <h1>{name}</h1>

			class App extends React.Component {
				state = { loggedIn: false }
				logIn = () => this.setState({loggedIn: true}) 
				logOut = () => this.setState({loggedIn: false}) 
				
				render(){
					return (
						<div>
							<button onClick={this.logIn}>log in</button>
							<button onClick={this.logOut}>log out</button>

							<div> The user is {this.state.loggedIn ? "logged in" : "not logged in"}. </div>
							<Lake name="Lake Taheo" />
							<Lake name="Verity lake" />
							<Lake name="Valor lake" />
							<Lake name="Acuity lake" />
						</div>
					)
				}
			}

			ReactDOM.render(
				<App/>,
				document.getElementById("root")
			)
		</script>-->


		<!-- Conditional use -->
		<!--<script type="text/babel">
			const Lake = ({name}) => <h1>{name} lake</h1>
			const SkiResort = ({name}) => <h1>{name}</h1>

			const App = ({summer}) => ( <div> {summer ? <Lake name="Acuity"/> : <SkiResort name="Alpine"/>} </div>)
			ReactDOM.render(
				<App summer={false}/>,
				document.getElementById("root")
			)
		</script>-->

		<!-- Array use -->
		<script type="text/babel">
			const lakeList = ["Echo Lake", "Verity Lake", "Valor Lake"]
			const Lake = ({name}) => <h1>{name} lake</h1>

			/* use key to help react to dynamic render */
			const App = ({lakes}) => ( <ul> {lakes.map((lake, i) => <li key={i}>{lake}</li>)} </ul>)
			
			ReactDOM.render(
				<App lakes={lakeList}/>,
				document.getElementById("root")
			)
		</script>
	</body>
	<style type="text/css">
		.welcomeHeading{
			color: blue;
		}
	</style>
</html>
```

## Use tools to coding with react

Install _create-react-app_ → `sudo npm install -g create-react-app`. Create project with command `create-react-app APP_NAME`. To run server use `npm start`.

Build React project with `npm run build`, in _build_ folder you can find your website ready to hosting. You can test your self with `npm install serve -g` and `serve -s build` 

## Requirement knowledge

* HTML CSS
* JavaScript
* ES6