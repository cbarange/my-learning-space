###### AUTHOR : Clément BARANGER  -  DATE : 10/03/2020

# Idea

> https://www.highcharts.com/demo/line-labels/dark-unica

# Setup
```bash
npm install -g http-server
http-server -c-1
http://localhost:8080/data.tsv
```

# Question

Image as JSON

# Google Image Chart API

> https://chart.googleapis.com/chart?cht=p3&chd=t:60,40&chs=250x100&chl=Hello|World

* cht : chart type
* chd : chart data t:60,40
* chs : chart size intxint
* chl : chart legend string|string
* chco: chart color FFC6A5|FFFF42|DEF3BD|00A5C6|DEBDDE

## Chart type

* Line Chart
* Scatter Chart
* Radar Chart
* Pie Chart
* Venn Chart
* Map Chart
* GraphViz Chart
* Google-O-meter Chart
* Compound Chart
* Candlestick Chart
* Box Chart
* Bar Chart

## Bar Charts
> https://developers.google.com/chart/image/docs/gallery/bar_charts
* Bar chart vertical
	* Premier exemple / Grouped
		* cht=bvg
		* chd=t:5,5,5|10,10,10|15,15,15
	* Second exemple / Stacked
		* cht=bvs
		* chd=t:5,5,5|10,10,10|15,15,15
	* Troisieme exemple / Overlapped
		* cht=bvo
		* chd=t:5,5,5|10,10,10|15,15,15
* Bar Chart Horizontal
	* Premier exemple / 
		* cht=bhs
		* chco=4D89F9,C6D9FD
		* chd=t:10,50,60,80,40|50,60,100,40,20


# D3JS et Data Driven Document

D3.js est une librairie Javascript libre et open-source très populaire, elle permet de manipuler des éléments HTML, SVG et CSS pour produire des graphiques, images, rendus dynamiques. Le principal problème de D3 est sont nombre de version, en 2020 il existe 5 version que n'offrent aucune rétro-compatibilité. Github : https://github.com/d3/d3.

> SHAPE DOC : https://github.com/d3/d3-shape/

## Installation
> Version utilisée : v5

On peut l'installer de plusieurs façons, depuis un package manager npm/yarn, l'utiliser en CDN, télécharger directement le d3.min.js. Ici je choisi de télécharger directement le fichier js, cela permet un controle plus rapide sur la version utilisée mais un gestion manuelle.

> CDN : `<script src="https://d3js.org/d3.v5.js"></script>` / `<script src="https://d3js.org/d3.v5.min.js"></script>`

> NPM : `npm install d3`

> .JS : https://d3js.org/d3.v5.js

## Utilisation

> Tuto(v4) : https://github.com/d3/d3/wiki/Tutorials

> Exemple : https://observablehq.com/@d3/gallery

> API : https://github.com/d3/d3/blob/master/API.md

### Premier utilisation
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>
<span>Hello</span><span>World</span><span> ! ! !</span>
<!-- Pour ceux qui ont deja utilise JQuery, cela leur sera famillie -->
<script type="text/javascript">
d3.selectAll("span").style("background-color", (d, i) => i % 2 ? "#EF4" : "#E4F" )
</script>

</body>
</html>
```

### Fonctionnement de D3
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>
<span id="d3-canvas"></span>

<p>Bonjour</p>
<p>comment</p>
<p>ca va</p>
<!-- Commente la ligne suivante et regarde ce qui se passe -->
<p> ? ¿ </p>

<script type="text/javascript">
	d3.select("body")
	.selectAll("p")
	.data([4, 8, 15, 16, 23, 42])
	.enter()
	.append("p")
	.text((i)=>`I'm ${i} !`)

	d3.select("#d3-canvas").append("p").text("Slt")
</script>
</body>
</html>
```

### Fonctionnement de D3 Bis
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<ul></ul>

<script type="text/javascript">
var fruits = ['apple', 'mango', 'banana', 'orange']

d3.select('ul')
	.selectAll('li')
	.data(fruits)
	.enter()
	.append('li')
	.text( (d) =>d )

</script>
</body>
</html>
```

### Animation
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<svg height="100" width="100">
  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
</svg> 

<script type="text/javascript">
	d3.select("body")
	.transition()
	.duration(2500)
	.style("background-color", "black")	

	d3.selectAll("circle").transition()
	.delay(2500)
	.duration(500)
	.attr("fill", "blue")
	.attr("stroke", () => "green")
	.attr("r",(d) => 10)
</script>
</body>
</html>
```

### Affichage de forme
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<span id="d3-canvas"></span>

<script type="text/javascript">
var canvas = d3.select("#d3-canvas") // D3 uses a jQuery like selector
	.append("svg")
	.attr("height", 500)
	.attr("width", 500)

var circle = canvas.append("circle") // Appending shape elements to the SVG element
	.attr("cx", 250)
	.attr("cy", 250)
	.attr("r", 100)
	.attr("fill", "red")

var rectangle = canvas.append("rect")
	.attr("height", 500).attr("width", 100)
	.attr("fill", "blue")
	.attr("stroke", "blue")
	.attr("stroke-width", 2)

var line = canvas.append("line")
	.attr("x1", 500).attr("y1", 0)
	.attr("x2", 500).attr("y2", 500)
	.attr("stroke-width", 2)
	.attr("stroke", "black")
</script>
</body>
</html>
```

### Utilisation de l'API
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>
<script type="text/javascript">
const data = [1, 2, 3, 4, 5];
const moreData = [[5, 20], [480, 90], [250, 50], [100, 33], [330, 95]];

console.log(d3.min(data)) // 1

console.log(d3.max(moreData, (d) =>d[0])) // 480

console.log(d3.max(moreData, (d) => d[1])) // 95

console.log(d3.extent(data)) // [1, 5]
</script>
</body>
</html>
```

### Scale
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<span id="d3-canvas"></span>

<script type="text/javascript">

const moreData = [[5, 20], [480, 90], [250, 50], [100, 33], [330, 95]]

var xScale = d3.scaleLinear()
    .domain([0, d3.max(moreData, (d) => d[0] )])
    .range([0, 500])

var yScale = d3.scaleLinear()
    .domain([0, d3.max(moreData, (d) => d[1] )])
    .range([500, 0]) // SVG is y-down


console.log(xScale(0))
console.log(xScale(480))

console.log(yScale(0))
console.log(yScale(95))
// The intermediate values are mapped linearly between 0 and 500.

// To create an axis, we just pass on our scale to the suitable axis function.
var xAxis = d3.axisBottom(xScale);
// About scale : https://github.com/d3/d3-scale

</script>
</body>
</html>
```

### Premier graphique

```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<button id="btn">Click ME !</button>
<br/><br/>
<svg height="100" width="200" onload="d3loaded()"></svg>

<script type="text/javascript">

var d3loaded = (color = "black") => {

	// Remove rect
	d3.select('svg').selectAll('*').remove()
	
	var data = [80, 120, 60, 150, 200]
	var barHeight = 20

	d3.select('svg')
	.selectAll('rect')
	.data(data)
	.enter()
	.append('rect')
	.attr('fill', color )
	.attr('width', (d) => d )
	.attr('height', barHeight - 1)
	.attr('transform', (d, i) => "translate(0," + i * barHeight + ")")
}
d3.select('#btn')
.on('click',() => {d3loaded("red");console.log("Clicked")})
</script>
</body>
</html>
```

### Le Pie Chart
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<svg height="100" width="200" onload="d3loaded()"></svg>

<script type="text/javascript">

var d3loaded = (color = "black") => {
	var sales = [ { product: 'Hoodie',  count: 12 }, { product: 'Jacket',  count: 7 }, { product: 'Snuggie', count: 6 },]
	var pie = d3.pie()
	.value( (d) => d.count)
	var slices = pie(sales)
	console.log(slices)

	var arc = d3.arc()
	.innerRadius(0)
	.outerRadius(50);

	// helper that returns a color based on an ID
	var color = d3.scaleOrdinal(d3.schemeCategory10);

	var svg = d3.select('svg').attr('width',300)
	var g = svg.append('g')
	.attr('transform', 'translate(200, 50)')

	g.selectAll('path.slice')
	.data(slices)
	.enter()
	.append('path')
	.attr('class', 'slice')
	.attr('d', arc)
	.attr('fill', (d) => color(d.data.product))

	// building a legend is as simple as binding
	// more elements to the same data. in this case,
	// <text> tags
	svg.append('g')
	.attr('class', 'legend')
	.selectAll('text')
	.data(slices)
	.enter()
	.append('text')
	.text((d) => '• ' + d.data.product)
	.attr('fill', (d) => color(d.data.product) )
	.attr('y', (d, i) => 20 * (i + 1) )
}

</script>
</body>
</html>
```

### Scatter Chart
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>
<div id="d3_area"></div>


<script type="text/javascript">


	// set the dimensions and margins of the graph
	var margin = {top: 10, right: 40, bottom: 30, left: 30},
	width = 450 - margin.left - margin.right,
	height = 400 - margin.top - margin.bottom;

	// append the svg object to the body of the page
	var svg = d3.select("#d3_area")
	.append("svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom)
	.append("g")
	.attr("transform", `translate(${margin.left},${margin.top})`);

	// Create data
	var data = [ {x:10, y:20}, {x:40, y:90}, {x:80, y:50} ]

	// X scale and Axis
	var x = d3.scaleLinear()
	.domain([0, 100])         // This is the min and the max of the data: 0 to 100 if percentages
	.range([0, width]);       // This is the corresponding value I want in Pixel
	
	svg.append('g')
	.attr("transform", `translate(0,${height})`)
	.call(d3.axisBottom(x));

	// X scale and Axis
	var y = d3.scaleLinear()
	.domain([0, 100])         // This is the min and the max of the data: 0 to 100 if percentages
	.range([height, 0]);       // This is the corresponding value I want in Pixel
	
	svg.append('g')
	.call(d3.axisLeft(y));

	// Add 3 dots for 0, 50 and 100%
	svg.selectAll("whatever")
	.data(data)
	.enter()
	.append("circle")
	.attr("cx", function(d){ return x(d.x) })
	.attr("cy", function(d){ return y(d.y) })
	.attr("r", 7)

</script>
</body>
</html>
```

### Line Chart
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<div id="my_dataviz"></div>

<script type="text/javascript">
// 2. Use the margin convention practice 
var margin = {top: 50, right: 50, bottom: 50, left: 50}
, width = window.innerWidth - margin.left - margin.right // Use the window's width 
, height = window.innerHeight - margin.top - margin.bottom // Use the window's height

// The number of datapoints
var n = 21

// 5. X scale will use the index of our data
var xScale = d3.scaleLinear()
.domain([0, n-1]) // input
.range([0, width]) // output

// 6. Y scale will use the randomly generate number 
var yScale = d3.scaleLinear()
.domain([0, 1]) // input 
.range([height, 0]) // output 

// 7. d3's line generator
var line = d3.line()
.x((d, i) => xScale(i) ) // set the x values for the line generator
.y((d) => yScale(d.y) ) // set the y values for the line generator 
.curve(d3.curveMonotoneX) // apply smoothing to the line

// 8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
var dataset = d3.range(n).map( (d) =>{return {"y": d3.randomUniform(1)()} })

// 1. Add the SVG to the page and employ #2
var svg = d3.select("body").append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform", `translate(${margin.left},${margin.top})`)

// 3. Call the x axis in a group tag
svg.append("g")
.attr("class", "x axis")
.attr("transform", `translate(0,${height})`)
.call(d3.axisBottom(xScale)) // Create an axis component with d3.axisBottom

// 4. Call the y axis in a group tag
svg.append("g")
.attr("class", "y axis")
.call(d3.axisLeft(yScale)) // Create an axis component with d3.axisLeft

// 9. Append the path, bind the data, and call the line generator 
svg.append("path")
.datum(dataset) // 10. Binds data to the line 
.attr("class", "line") // Assign a class for styling 
.attr("d", line) // 11. Calls the line generator 
.style("fill","none")
.style("stroke","#ffab00")
.style("stroke-width",3)

// 12. Appends a circle for each datapoint 
svg.selectAll(".dot")
.data(dataset)
.enter()
.append("circle") // Uses the enter().append() method
.attr("class", "dot") // Assign a class for styling
.attr("cx", (d, i) => xScale(i) )
.attr("cy", (d) => yScale(d.y) )
.attr("r", 5)
.style("fill","#ffab00")
.style("stroke","#fff")
.on("mouseover", (a, b, c) => {console.log(a); d3.select(event.currentTarget).style("fill", "steelblue").style("cursor","crosshair")})
.on("mouseout", () => { d3.select(event.currentTarget).style("fill", "#ffabFF") })
</script>
</body>
</html>
```

### Tooltips
```xml
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>First Usage</title>
	<script type="text/javascript" src="../d3.js"></script>
</head>
<body>

<div id="container" style="width: 100%;height: 100%;">
	<div id="chart"></div>
</div>

<script type="text/javascript">
const margin = {top: 20, right: 30, bottom: 30, left: 60},
	width = document.getElementById("container").offsetWidth * 0.95 - margin.left - margin.right,
	height = 400 - margin.top - margin.bottom

const parseTime = d3.timeParse("%d/%m/%Y")
const dateFormat = d3.timeFormat("%d/%m/%Y")

const x = d3.scaleTime().range([0, width])

const y = d3.scaleLinear().range([height, 0])

const line = d3.line()
		.x((d) => x(d.date) )
		.y((d) => y(d.close) )

const svg = d3.select("#chart")
	.style("margin-top","20px")
	.style("border","1px solid #DEDEDE")
	.append("svg")
    .attr("id", "svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .style("display","block")
    .style("margin","auto")
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`)

// On demande à D3JS de charger notre fichier
// On déclare également une map qui servira un peu plus bas pour l'affichage du tooltip
var map = {}
d3.tsv("http://localhost:8080/data.tsv").then(function(data) {
    // Conversion des données du fichier, parsing des dates et '+' pour expliciter une valeur numérique.
    data.forEach(function(d) {
        d.date = parseTime(d.date)
        d.close = +d.close
        d.volume = +d.volume
        map[d.date] = d // sauvegarde sous forme de hashmap de nos données.
    })
    
    // Contrairement au tutoriel Bar Chart, plutôt que de prendre un range entre 0 et le max on demande 
    // directement à D3JS de nous donner le min et le max avec la fonction 'd3.extent', pour la date comme 
    // pour le cours de fermeture (close).
    x.domain(d3.extent(data, (d) => d.date ))
    y.domain(d3.extent(data, (d) => d.close ))

    // Ajout de l'axe X
    svg.append("g")
	.attr("transform", `translate(0,${height})`)
	.call(d3.axisBottom(x))

    // Ajout de l'axe Y et du texte associé pour la légende
    svg.append("g")
	.call(d3.axisLeft(y))
	.append("text")
	.attr("fill", "#000")
	.attr("transform", "rotate(-90)")
	.attr("y", 6)
	.attr("dy", "0.71em")
	.style("text-anchor", "end")
	.text("Pts")
	
	// Ajout de la grille horizontale (pour l'axe Y donc). Pour chaque tiret (ticks), on ajoute une ligne qui va 
	// de la gauche à la droite du graphique et qui se situe à la bonne hauteur.
    svg.selectAll("y axis").data(y.ticks(10)).enter()
	.append("line")
	.attr("class", "horizontalGrid")
	.attr("x1", 0)
	.attr("x2", width)
	.attr("y1", (d) => y(d))
	.attr("y2", (d) => y(d))
	.style("fill","none")
	.style("shape-rendering","crispEdges")
	.style("stroke","lightgrey")
	.style("stroke-width","1px")
	

    
    // Ajout d'un path calculé par la fonction line à partir des données de notre fichier.
    svg.append("path")
	.datum(data)
	.attr("class", "line")
	.attr("d", line)
	.style("fill","none")
	.style("stroke","steelblue")
	.style("stroke-width","1.5px")

})

var div = d3.select("body").append("div")   
		.attr("class", "tooltip")
		.attr("x", width - 300)
		.attr("y", 0)
		.style("opacity", 0)

var verticalLine = svg.append("line")
		.attr("class", "verticalLine")
		.attr("x1",0)
		.attr("y1",0)
		.attr("x2",0)
		.attr("y2",height)
		.style("opacity", 0)
		.style("fill", "none")
		.style("shape-rendering", "ncrispEdgesone")
		.style("stroke", "lightgrey")
		.style("stroke-width", "1px")
	 

d3.select("#chart").on("mousemove", function() {
    // Récupération de la position X & Y de la souris.
    var mouse_x = d3.mouse(this)[0]
    var mouse_y = d3.mouse(this)[1]
    
    // Si la position de la souris est en dehors de la zone du graphique, on arrête le traitement
    if (mouse_x < margin.left || mouse_x > (width + margin.left) || mouse_y < margin.top || mouse_y > (400 - margin.bottom))
        return
    
    // Grâce à la fonction 'invert' nous récupérons la date correspondant à notre position
    // A noter, il faut soustraire la marge à gauche pour que la valeur soit correct.
    var selectedDate = x.invert(mouse_x - margin.left)
    
    // Positionnement de la barre verticale toujours en tenant compte de la marge
    verticalLine.attr("x1", mouse_x - margin.left)
    verticalLine.attr("x2", mouse_x - margin.left)
    verticalLine.style("opacity", 1)
    
    // Le revert est précis à la milliseconde, ce qui n'est pas le cas de nos données
    selectedDate.setHours(0,0,0,0)
    var entry = map[selectedDate]
    if (typeof entry === "undefined")
        return

    // Si une entrée existe pour la date sélectionnée nous pouvons afficher les données.
    
    // Le comportement est équivalent aux précédents exemples pour le tooltip.
    div.style("opacity", .9)
    div.style("left", (d3.event.pageX + 30) + "px")     
        .style("top", (d3.event.pageY - 60) + "px")
        .html(`<b>Date : </b> ${dateFormat(entry.date)}<br><b>Cours : </b>${entry.close}<br><b>Volume : </b>${entry.volume}<br>`)
}).on("mouseout", function() {
   	var mouse_x = d3.mouse(this)[0]
   	var mouse_y = d3.mouse(this)[1]
	// Si la position de la souris est en dehors de la zone du graphique, on masque la ligne et le tooltip
   	if (mouse_x < margin.left || mouse_x > (width + margin.left) || mouse_y < margin.top || mouse_y > (400 - margin.bottom)) {
       	div.style("opacity", 0)
       	verticalLine.style("opacity", 0)
   	}
})

</script>

<style type="text/css">
.tooltip {
	position: absolute;
	opacity:0.8;
	z-index:1000;
	text-align:left;
	border-radius:4px;
	-moz-border-radius:4px;
	-webkit-border-radius:4px;
	padding:8px;
	color:#fff;
	background-color:#000;
	font: 12px sans-serif;
	max-width: 300px;
	height: 53px;	
}
</style>

</body>
</html>

<!--
http://datawanderings.com/2019/11/01/tutorial-making-an-interactive-line-chart-in-d3-js-v-5/
http://datawanderings.com/2019/10/28/tutorial-making-a-line-chart-in-d3-js-v-5/
https://stackoverflow.com/questions/23218174/how-do-i-save-export-an-svg-file-after-creating-an-svg-with-d3-js-ie-safari-an
https://www.datavis.fr/index.php?page=linearchart-improve
https://www.datavis.fr/index.php?page=linearchart
https://bl.ocks.org/gordlea/27370d1eea8464b04538e6d8ced39e89
https://github.com/d3/d3-shape/
https://www.highcharts.com/demo/line-labels/dark-unica
-->
```

### _
```xml

```
