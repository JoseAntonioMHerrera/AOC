use std::vec::Vec;
use std::fmt;
use std::io::{self, BufRead,Error};
use std::fs::File;
use std::path::Path;

pub struct Terrain{
	map: Vec<String>,
	row: usize,
	column: usize,
	horizontal_shift: usize,
	vertical_shift: usize
}
impl Terrain {
	pub fn new(filename: String,row:usize,column:usize,horizontal_shift:usize,vertical_shift:usize) -> Result<Terrain,Error> {
		let path = Path::new(&filename);
		println!("{}", path.display());
		let file = File::open(&path)?;
    	let lines = io::BufReader::new(file).lines();
    	let mut map: Vec<String> = Vec::new();
    	for line in lines {
    		if let Ok(l) = line{
    			map.push(l);
    		}
    	};
    	Ok(Terrain {map,row,column,horizontal_shift,vertical_shift})
	}

	pub fn mutHorizontalShift(&mut self) -> &mut usize{
		&mut self.horizontal_shift
	}

	pub fn mutVerticalShift(&mut self) -> &mut usize{
		&mut self.vertical_shift
	}

	pub fn mutResetRow(&mut self) -> &mut usize{
		&mut self.row
	}

	pub fn mutResetColumn(&mut self) -> &mut usize{
		&mut self.column
	}
}

impl Iterator for Terrain {
	type Item = char;

	fn next(&mut self) -> Option<Self::Item>{
		while self.row < self.map.len() - 1 {
			self.column += self.horizontal_shift;
			self.row += self.vertical_shift;
			let new_column_position = ((self.column % (self.map[self.row].len())) +
				(self.map[self.row].len()) ) % (self.map[self.row].len());
			let step:char = self.map[self.row].chars().nth(new_column_position).unwrap();
			return Some(step); 
		}
		None
	}
}

impl fmt::Display for Terrain {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
    	let mut output_map:String = "".to_string();
    	for line in &self.map{
    		output_map.push_str(&(line.to_owned()+"\n")); // .to_owned()???
    	};
    	write!(f, "{}", output_map)
    }
}