//This header is from https://github.com/googlearchive/tango-examples-unity/blob/master/TangoWithMultiplayer/Assets/Photon%20Unity%20Networking/Plugins/PhotonNetwork/PhotonClasses.cs

public struct PhotonMessageInfo
{
    private readonly int timeInt;
    public readonly PhotonPlayer sender;
    public readonly PhotonView photonView;

    public PhotonMessageInfo(PhotonPlayer player, int timestamp, PhotonView view)
    {
        this.sender = player;
        this.timeInt = timestamp;
        this.photonView = view;
    }

    public double timestamp
    {
        get
        {
            uint u = (uint)this.timeInt;
            double t = u;
            return t / 1000;
        }
    }

    public override string ToString()
    {
        return string.Format("[PhotonMessageInfo: Sender='{1}' Senttime={0}]", this.timestamp, this.sender);
    }
}