
d3.json("images.json", function(error, paths) {
	var nested = d3.select("body").selectAll("div")
	    .data(paths).enter().append("div")
	    .each(function (row, i) {
		    var nPhotos = row.length;
		    d3.select(this).selectAll("img")
		    .data(row).enter().append("img")
		    .attr("src", function(d) {
			    return d.path;
			})
		    .style("-webkit-transform", function(d, j) {
			    var step = 5;
			    return "rotate(" + ( (j - nPhotos/2 + 1) * step) + "deg)";
			})
		    .style("-webkit-filter", function(d, j) {
			    if ((i + j) % 3 === 0) {
				return "saturate(-1) contrast(90%)";
			    } else if ((i + j) % 3 === 1) {
				return "saturate(-1)";
			    } else {
				return "contrast(90%)";
			    }
			});
		});
});
