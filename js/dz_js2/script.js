document.writeln("</table>");

document.writeln("<table border='1' width='300'>")
document.writeln("<tr align='center'>")
for(let i=1; i<11; i++){
    for (let j=1; j<11; j++){
        if((i + j) % 2 == 0){
        document.writeln("<td bgcolor='red'>"+ i * j+ "</td>")
        } else{
             document.writeln("<td bgcolor='yellow'>"+ i * j+ "</td>")
        }
    }
    document.writeln("</tr>")
}
document.writeln("</table>")