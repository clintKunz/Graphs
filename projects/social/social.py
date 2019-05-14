import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")
        # Create friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID+1, self.lastID+1):
                possibleFriendships.append((userID, friendID))

        # Shuffle
        random.shuffle(possibleFriendships)

        # Add friends
        for friendship_index in range(avgFriendships * numUsers // 2):
            friendship = possibleFriendships[friendship_index]
            self.addFriendship(friendship[0], friendship[1])


    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # bft to get all connections in keys of directory
        q = Queue()
        visited = {}
        q.enqueue(userID)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.update({v: []})
                for friend in self.friendships[v]:
                    q.enqueue(friend)
        
        
        for friend in visited:
            if userID is not friend:
                path = self.bfs(userID, friend)
                visited.update({friend: path})
            else: 
                visited.update({userID: [userID]})

        return visited

    # bfs to get shortest path as value in dictionary
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex])

        while q.size() > 0:
            v = q.dequeue()
            node = v[-1]

            if node not in visited:
                for neighbor in self.friendships[node]:
                    path = list(v)
                    path.append(neighbor)
                    q.enqueue(path)
                    if neighbor == destination_vertex:
                        return path
                
                visited.add(node)    


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

