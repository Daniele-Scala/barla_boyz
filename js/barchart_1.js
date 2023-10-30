d3.json("dataset1.json").then(function(data) {
    console.log(data); // Add this line for debugging
  var citySelector = d3.select("#city-selector");
  var cities = [...new Set(data.map(d => d.city))];

  citySelector
    .selectAll("option")
    .data(cities)
    .enter()
    .append("option")
    .attr("value", d => d)
    .text(d => d);

  function updateBarChart(city) {
    var filteredData = data.filter(d => d.city === city);
    var treeCounts = {};

    filteredData.forEach(function(d) {
      if (treeCounts[d.scientific_name]) {
        treeCounts[d.scientific_name] += d.count;
      } else {
        treeCounts[d.scientific_name] = d.count;
      }
    });

    var svg = d3.select("#bar-chart");
    svg.html(""); // Clear the previous content

    var margin = { top: 20, right: 20, bottom: 30, left: 40 };
    var width = 800 - margin.left - margin.right;
    var height = 400 - margin.top - margin.bottom;

    var chart = svg.append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleBand()
      .range([0, width])
      .padding(0.1)
      .domain(Object.keys(treeCounts));

    var y = d3.scaleLinear()
      .range([height, 0])
      .domain([0, d3.max(Object.values(treeCounts))]);

    chart.selectAll(".bar")
      .data(Object.entries(treeCounts))
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", d => x(d[0]))
      .attr("y", d => y(d[1]))
      .attr("width", x.bandwidth())
      .attr("height", d => height - y(d[1]));

    chart.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    chart.append("g")
      .call(d3.axisLeft(y));
  }

  updateBarChart(cities[0]);

  citySelector.on("change", function() {
    var selectedCity = this.value;
    updateBarChart(selectedCity);
  });
});