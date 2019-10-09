lambda_name=hello-world-apig-wsgi

# Example:
libs/: requirements.txt requirements-test.txt
  $@   # refers to target: "libs/"
  $<   # refers to the first prerequisite: "requirements.txt"
  $^   # refers to all prerequisites: "requirements.txt requirements-test.txt"

libs: requirements.txt
	@[ -d $@ ] || mkdir $@
		pip install -r $< -t $@

output.zip: libs
	zip -r $@ *.py # zip all python source code into output.zip
	cd $< &&  zip -rm ../$@ * # zip libraries installed in the libs dir into output.zip
	rmdir libs


deploy: output.zip
	-aws lambda update-function-code \
		--function-name ${lambda_name} \
		--zip-file fileb://$<

clean:
	rm output.zip

all: deploy output.zip clean