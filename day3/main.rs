use std::process;
use day3::Terrain;

fn main() {
    let mut terrain = Terrain::new("input.txt".to_string(),0,0,0,0).unwrap_or_else( |err| {
    	println!("Problem reading filename: {}",err);
    	process::exit(1);
    });

    let shifts = vec![(1,1),(3,1),(5,1),(7,1),(1,2)];
    let mut trees_counter = 0;
    let mut arboreal_product:u64 = 1;

    for shift in shifts{
    	*terrain.mutHorizontalShift() = shift.0;
    	*terrain.mutVerticalShift() = shift.1;
    	while let Some(slot) = terrain.next() {
    		match slot {
    			'#' => trees_counter+=1,
    			_ => (),
    		}		
    	}
    	println!("Number of trees encountered: \n {}",trees_counter);
    	arboreal_product = arboreal_product*trees_counter;
    	trees_counter=0;
    	*terrain.mutResetRow() = 0;
    	*terrain.mutResetColumn() = 0;
    }

    println!("Product of trees: \n {}",arboreal_product);
    
}
