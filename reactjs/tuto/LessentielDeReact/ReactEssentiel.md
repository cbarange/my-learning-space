###### AUTEUR : Clement BARANGER	DATE : 03/01/2020	SOURCE : https://www.linkedin.com/learning/l-essentiel-de-react-js-2/ | Damien BRUYNDONCKX

# L'essentiel de React.js

## Introduction

Bibliothèque Javascript créée par facebook, rendu open source en 2013. C'est une librairie très utilisé dans l'industrie. 

## Installation et Setup

Installer l'extension React Developpers Tools sur votre navigateur

## ES6

Avec le mot cle `var`les variable sont globals, a la difference de `let` qui definit les variables pour un seul bloc de code
```js
var add = () => (2 * 4)

var add = () => {return 2 * 4}

function add(){return 2 * 4}

// ------------------
var colors = ['red','blue']
var newColors = colors.concat('green')

var newColors = [...colors, 'green']
```

## Composent fonctionnel
```js
const Bonjour = () => <h1>Bonjour sur React</h1>
ReactDOM.render(<Bonjour/>, document.getElementById('react-root'))
```

## Component class et fonctionnel
```js
class BonjourClass extends React.Component {
            render(){
                return (
                    <div id="title">
                        <h1 className="heading">{this.props.message}</h1>
                        <p>Vous apprenez la version {this.props.version} de Réact.</p>
                    </div>
                )
            }
        }

        const Bonjour = ({message, version}) => (
            <div id="title">
                    <h1 className="heading">{message}</h1>
                    <p>Vous apprenez la version {version} de Réact.</p>
            </div>
        )

        ReactDOM.render(
            <Bonjour message="Bonjour de Réact 16" version={16} />, 
            document.getElementById('react-root')
        )
```

## Rendu dynamique

```js
class Bonjour extends React.Component {
	constructor(props){
		super(props)
		this.state={
			name='damien'
		}
		this.handleChange = this.handleChange.bind(this)
	}

	handleChange(e){
		this.setState({name : e.target.value})
	}

	render(){
		return {
			<div id="title">
				<h1>{this.props.message}</h1>
				<p>Bonjour {this.state.name} </p>
				<p><input type="text" value={this.state.name} onChange={this.handleChange} /> </p>
			</div>
		}
	}
}
ReactDOM.render(
	<Bonjour message="Bonjour de Réact 16" />, 
	document.getElementById('react-root')
)
```

## Create React App

```shell
npm install create-react-app
create-react-app PROJECT_NAME
cd PROJECT_NAME
npm install
npm start
```

## Multi root

Pour utiliser plusieur elements racines dans un component on utilise : <React.Fragment> <h1></h1> <p></p> </React.Fragment>, simplifié en <> <h1></h1> <p></p> </>

## React-Router

Installation avec `npm install react-router-dom --save`, --save permet d'enregistrer la dependance dans le packages.json. 

```js
import {BroswerRouter, Switch Route} from 'react-router-dom'

class App extends React.Component{
	render(){
		<BroswerRouter>
			<Switch>
				<Route path="/add-task" component={AddTask} />
				<Route path="/" component={ToDoList} />
			</Switch>
			<NavBar />
		</BroswerRouter
	}
}
```    

```js
import {NavLink} from 'react-router-dom'

const NavBar = () => <div><NavLink to="/">Click Here</NavLink> <NavLink to="/add-task">Add</NavLink> </div>
```

Route parametré
```js
<Route path="/:filter?" component={ToDoList} />
```

```js
<Route path="/:filter?" render={(props) => <ToDoList {...props} tasks={initialData} />} />
```

```js

```

```js

```

```js

```