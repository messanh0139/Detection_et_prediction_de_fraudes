_```markdown
# Schéma de données

## Table: transactions

| Colonne | Type | Description |
|---|---|---|
| `transaction_id` | `INTEGER` | Identifiant unique de la transaction (clé primaire) |
| `distance_from_home` | `FLOAT` | Distance entre le lieu de la transaction et le domicile du titulaire de la carte |
| `distance_from_last_transaction` | `FLOAT` | Distance entre le lieu de la transaction et le lieu de la transaction précédente |
| `ratio_to_median_purchase_price` | `FLOAT` | Ratio du montant de la transaction par rapport au prix d'achat médian |
| `repeat_retailer` | `BOOLEAN` | Indique si le titulaire de la carte a déjà effectué un achat chez ce commerçant |
| `used_chip` | `BOOLEAN` | Indique si la transaction a été effectuée avec la puce de la carte |
| `used_pin_number` | `BOOLEAN` | Indique si le code PIN a été utilisé pour la transaction |
| `online_order` | `BOOLEAN` | Indique si la transaction a été effectuée en ligne |
| `fraud` | `BOOLEAN` | Indique si la transaction est frauduleuse |

_```

