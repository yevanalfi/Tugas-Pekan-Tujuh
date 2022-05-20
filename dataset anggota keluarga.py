{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "dd4241ff-a674-4435-814a-450aa3f6a13d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nama</th>\n",
       "      <th>Tinggi Badan</th>\n",
       "      <th>Berat Badan</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Amir</td>\n",
       "      <td>120</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Fadli</td>\n",
       "      <td>145</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Fatya</td>\n",
       "      <td>165</td>\n",
       "      <td>65</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Nama  Tinggi Badan  Berat Badan\n",
       "0   Amir           120           20\n",
       "1  Fadli           145           40\n",
       "2  Fatya           165           65"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "pizza = {'Nama': ['Amir', 'Fadli', 'Fatya'],\n",
    "'Tinggi Badan': [120, 145, 165],\n",
    "'Berat Badan': [20, 40, 65]\n",
    "}\n",
    "\n",
    "pizza_df = pd.DataFrame(pizza)\n",
    "pizza_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "808292cc-c366-490a-8f02-8bf145dbbd37",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
