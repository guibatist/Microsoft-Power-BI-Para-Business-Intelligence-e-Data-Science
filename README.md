# Manipulação com Power Query M Language

// Substituindo Valor
"Valor Substituido" = Table.ReplaceValue(#"Ultima Operação", "?", "45", Replacer.ReplaceText,{"Idade"}),

// Removendo Coluna
"Coluna Removida" = Table.RemoveColumns(#"Valor Substituido",{"Estado Civil"})

// Adicionando Coluna
"Coluna Adicionada" = Table.AddColumn(#"Coluna Removida", "Valor Final" , each [Valor Compra] - [Valor Desconto])

// Dividindo Coluna
"Dividir Coluna pela Posição" = Table.SplitColumn(#"Coluna Adicionada", "ID_Cliente", Splitter.SplitTextByPositions({0, 4}, false), {"ID_Cliente.1", "ID_Cliente.2"}),
"Coluna Dividida" = Table.TransformColumnTypes(#"Dividir Coluna pela Posição", {{"ID_Cliente.1", type text}, {"ID_Cliente.2", Int64.Type}})

// Ajustando Nome Coluna
"Colunas Renomeadas" = Table.RenameColumns(#"Coluna Dividida", {{"ID_Cliente.1", "Código"}, {"ID_Cliente.2", "ID"}})

// Coluna Condicional
"Coluna Condicional Adicionada" = Table.AddColumn(#"Colunas Renomeadas", "% Desconto Especial", each if [Tipo de Cliente] = "Bronze" then 5 else if [Tipo de Cliente] = "Prata" then 10 else if [Tipo de Cliente] = "Ouro" then 15 else if [Tipo de Cliente] = "Diamante" then 20 else 0)

// Ajustando a escala de dados com Transformação Logaritimica
"Logaritmo de Base 10 Calculado" = Table.TransformColumns(#"Coluna Condicional Adicionada", {{"Limite de Credito", Number.Log10, type number}})
