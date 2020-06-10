
setOption("BlackBackground", false);
run("Make Binary");
run("Remove Outliers...", "radius=2 threshold=50 which=Bright");
run("Remove Outliers...", "radius=2 threshold=50 which=Bright");
setAutoThreshold("Default");
//run("Threshold...");
