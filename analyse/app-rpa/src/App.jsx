import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
    const [formData, setFormData] = useState({
        name: '',
        price: '',
        profit: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Données soumises:', formData);

        try {
            // Envoyer les données au serveur
            await axios.post('http://localhost:5000/api/save', formData);
            console.log('Données enregistrées avec succès');

            // Réinitialiser le formulaire après soumission
            setFormData({
                name: '',
                price: '',
                profit: ''
            });
        } catch (error) {
            console.error('Erreur lors de l\'enregistrement des données:', error);
        }
    };

    return (
        <div>
            <h1>Formulaire de Saisie</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Nom :</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="price">Prix :</label>
                    <input
                        type="number"
                        id="price"
                        name="price"
                        value={formData.price}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="profit">Bénéfice :</label>
                    <input
                        type="number"
                        id="profit"
                        name="profit"
                        value={formData.profit}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Soumettre</button>
            </form>
        </div>
    );
};

export default App;
