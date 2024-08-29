# test
puts "hello world"
class TheClass
	@@v = 3
	def init()
		puts "init"
	end
	def value
		@@v
	end
end

y = TheClass.new
puts "result=",y.value;

myv2='this is a string'
File.write('toto',myv2)

myv = File.read('toto')
puts myv

if myv.eql? myv2 
then
	puts "equal"
else
	puts "different"
end


