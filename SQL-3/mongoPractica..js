//show dbs;
db;
//use Cursos;

db.alumno.insertOne({
    nombre: "Juan Pérez",
    edad: 22,
    carrera: "Estadística"
})


db.alumno.find().pretty()

db.curso.insertMany([{
        nombre: "Probabilidad II",
        creditos: 10,
        horas: {
            teoria: 6,
            practica: 4
        }
    },
    {
        nombre: "Estadística Inferencial",
        creditos: 8,
        horas: {
            teoria: 5,
            practica: 3
        }
    },
    {
        nombre: "Bases de Datos",
        creditos: 12,
        horas: {
            teoria: 4,
            practica: 8
        }
    }
])



db.curso.find()


db.curso.find().pretty()


db.curso.find({
    creditos: 10
})


db.curso.find({
    creditos: 10,
    nombre: "Probabilidad II"
})


db.curso.find({
    "horas.practica": 4
})


db.curso.findOne({
    nombre: "Bases de Datos"
})

db.curso.find({}, {
    nombre: 1,
    creditos: 1,
    _id: 0
})


db.curso.find().sort({
    nombre: 1
})

db.curso.find().sort({
    creditos: -1
})

db.curso.find().limit(2)



db.curso.countDocuments()

db.curso.countDocuments({
    creditos: {
        $gt: 8
    }
})



db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $set: {
        departamento: "Estadística"
    }
})

db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $inc: {
        creditos: 2
    }
})

db.curso.updateMany({}, {
    $rename: {
        "horas": "horasSemanales"
    }
})

db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $unset: {
        departamento: ""
    }
})


db.curso.deleteOne({
    nombre: "Bases de Datos"
})


db.curso.drop()

db.dropDatabase()


db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $push: {
        temas: "Distribuciones"
    }
})


db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $pull: {
        temas: "Distribuciones"
    }
})

db.curso.updateOne({
    nombre: "Probabilidad II"
}, {
    $addToSet: {
        temas: "Probabilidad"
    }
})
db.curso.createIndex({
    nombre: 1
})
db.curso.getIndexes()

db.curso.createIndex({
    nombre: 1
})
db.curso.getIndexes()


db.curso.aggregate([{
    $match: {
        creditos: {
            $gte: 10
        }
    }
}])

db.curso.aggregate([{
    $group: {
        _id: "$creditos",
        totalCursos: {
            $sum: 1
        }
    }
}])

db.curso.aggregate([{
    $sort: {
        creditos: -1
    }
}])

db.curso.aggregate([{
    $project: {
        _id: 0,
        nombre: 1,
        creditos: 1,
        horasTotales: {
            $add: ["$horas.teoria", "$horas.practica"]
        }
    }
}])

db.curso.aggregate([{
    $count: "totalDocumentos"
}])

db.curso.aggregate([{
        $match: {
            creditos: {
                $gte: 8
            }
        }
    },
    {
        $group: {
            _id: "$creditos",
            cantidad: {
                $sum: 1
            }
        }
    },
    {
        $sort: {
            _id: 1
        }
    }
])