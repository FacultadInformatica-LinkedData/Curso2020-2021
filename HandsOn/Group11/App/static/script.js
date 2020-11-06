 $.getJSON("./query.json",{format: "json"},function(data){
                     $.each(data,function(index,value){
                         console.log(value);
                                $('#resultados',function(){
                                    $('#cuerpo-tabla').append('<tr>'+                  
                                        '<td>'+value.addressFullName+'</td>'+
                                        '<td>'+value.isOpen+'</td>'+
                                        '<td>'+value.itStarts+'</td>'+
                                        '<td>'+value.itEnds+'</td>'+
                                        '<td>'+value.hasLatitude+', '+value.hasLongitude+'</td>'                      
                                    +'</tr>')
                                })
                            })
                    })