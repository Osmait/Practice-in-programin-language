package readyaml

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"gopkg.in/yaml.v3"
)

type FontConfig struct {
	Font Font `yaml:"font"`
}

type Font struct {
	Normal     Normal `yaml:"normal" json:"normal"`
	Bold       Bold   `yaml:"bold" json:"bold"`
	Italic     Bold   `yaml:"italic" json:"italic"`
	BoldItalic Bold   `yaml:"bold_italic" json:"bold_italic"`
	Size       int64  `yaml:"size" json:"size"`
}

type Bold struct {
	Family string `yaml:"family"`
}

type Normal struct {
	Family   string   `yaml:"family"`
	Features []string `yaml:"features"`
}

func ReadYAml(num int) {
	dir, _ := os.Getwd()
	fmt.Println(dir)
	filePath := "./fond.yaml"

	yamlFoile, err := ioutil.ReadFile(filePath)
	if err != nil {
		log.Fatalf("Error al leer el archivo: %v", err)
	}
	var fontConfig FontConfig

	err = yaml.Unmarshal(yamlFoile, &fontConfig)

	if err != nil {
		log.Fatalf("Error deserializando el YAMl: %v", err)
	}

	fontConfig.Font.Size = int64(num)
	modif, err := yaml.Marshal(&fontConfig)
	if err != nil {
		log.Fatal("Error Guardando ")
	}
	err = ioutil.WriteFile(filePath, modif, 0644)

	if err != nil {
		log.Fatalf("Error al escribir  el archivo %v", err)
	}
	fmt.Println("Archivo guardado exitosamente.")
}
