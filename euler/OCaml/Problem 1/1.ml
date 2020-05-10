(* 
 *Finds the sum of two integer multiples below a certain limit. Program 
 *receives input as command line arguments where first argument is the first
 *multiple, second argument is the second multiple, and third argument is the
 *limit. Solution found in O(1) time complexity.
 *)

open Array;;
open Printf;;

(* Finds the sum of all real numbers up until the limit *)
let summation limit =
  limit *. ((limit +. 1.0) /. 2.0);;

(* Gives back the sum of all multiples of a number below a certain limit *)
let multiples_sum multiple limit =
  multiple *. summation(floor (limit /. multiple));;

let main () =

  (* Retrieve user input *)
  let [| multiple1; multiple2; limit |] = 
    map float_of_string (sub Sys.argv 1 3) in

  (* Find sum of each multiple and the sum of the product of both multiples *)
  let multiple1_sum = multiples_sum multiple1 (limit -. 1.0) in
  let multiple2_sum = multiples_sum multiple2 (limit -. 1.0) in
  let product_sum = multiples_sum (multiple1 *. multiple2) (limit -. 1.0) in
  let result = int_of_float (multiple1_sum +. multiple2_sum -. product_sum) in

  printf "The answer is: %d\n" result;
  exit 0;;

main ();;
